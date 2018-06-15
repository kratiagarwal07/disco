import os, subprocess, time, sys, re, cv2
from label_image import classify
from img_match import match, run, format
from text_match import textMatch
from img_download import download
from ocr_reader import google_ocr
from multiprocessing import Process, Pipe, Pool
from glob import glob
from flask import jsonify

ocr_category = ["book"]
subcategory = ["cycle"]

def imgMatch(category, filename):
    train = cv2.imread(filename)
    category = "/home/intel/FlaskApp/CampusHaat/classification/files/images/" + category
    arr = glob(category + '/*')
    print arr, category
    result = []
    for i in range((len(arr)/8)):

	pconn0, cconn0 = Pipe()
	pconn1, cconn1 = Pipe()
	pconn2, cconn2 = Pipe()
	pconn3, cconn3 = Pipe()
	pconn4, cconn4 = Pipe()
	pconn5, cconn5 = Pipe()
	pconn6, cconn6 = Pipe()
	pconn7, cconn7 = Pipe()

	prog0 = Process(target=run, args=(train, arr[8*i+0], cconn0))
	prog1 = Process(target=run, args=(train, arr[8*i+1], cconn1))
	prog2 = Process(target=run, args=(train, arr[8*i+2], cconn2))
	prog3 = Process(target=run, args=(train, arr[8*i+3], cconn3))
	prog4 = Process(target=run, args=(train, arr[8*i+4], cconn4))
	prog5 = Process(target=run, args=(train, arr[8*i+5], cconn5))
	prog6 = Process(target=run, args=(train, arr[8*i+6], cconn6))
	prog7 = Process(target=run, args=(train, arr[8*i+7], cconn7))

	prog0.start()
	prog1.start()
	prog2.start()
	prog3.start()
	prog4.start()
	prog5.start()
	prog6.start()
	prog7.start()

	ptemp = [pconn0, pconn1, pconn2, pconn3, pconn4, pconn5, pconn6, pconn7]
	for parent in ptemp:
		result.append(parent.recv())

        prog0.join()
	prog1.join()
	prog2.join()
	prog3.join()
	prog4.join()
	prog5.join()
	prog6.join()
	prog7.join()

    result = sorted(result, key = lambda x : x['Result'], reverse=True)
    temp = {"Image_res": result[0]["Img"],"Image_score": result[0]["Result"]/1000.0}
    return temp


def classification(conn, model, label, imagepath):
	label, result = classify(imagepath, model, label)
	print label, result
	if result > .8:
		conn.send(label)
		conn.close()
	else:
		conn.send("can't classify this item")



def textDetection(conn, conn1, imagepath):
	text = google_ocr(imagepath).lower()
	result = conn1.recv()
	if text == "no":
		conn.send([{}, result])
		conn.close()
	else:
		text = re.sub(r'\W+', ' ', text)
		score, title,result_id= textMatch(3, text)
		temp = {"Item_class":result ,"Ocr_text":text, "Ocr_title":title, "Ocr_score" : score, "prod_id":result_id}
		temp = [temp, result]
		conn.send(temp)
		conn.close()

# trying to run in parallel, two pipes for getting intermediate result
def class_run(imagepath, model, label):
    time1 = time.time()
    if "http" in imagepath:
	    imagepath = download(imagepath)
	    format(imagepath)
	    imagepath += ".jpg"
    parent_conn, child_conn = Pipe()
    parent_conn1, child_conn1 = Pipe()
    parent_conn2, child_conn2 = Pipe()
    p = Process(target=classification, args=(child_conn, model, label, imagepath))
    p1 = Process(target=textDetection, args=(child_conn2, parent_conn, imagepath))
    p.start()
    p1.start()
    result = parent_conn2.recv()
    text_res =  result[0]
    result =  result[1]
    p.join()
    p1.join()
    img_res =  imgMatch(result, imagepath)
    text_res.update(img_res)
    return text_res
