from flask import Flask, render_template, request, send_from_directory, redirect, current_app,  session, jsonify
import os, sys, subprocess, random
from werkzeug import secure_filename
from class_testing import class_run
from menu_scan_branch import run
#import class_testing
from menu_scan import menu_scanner
from ocr_reader import google_ocr
from news_utils import tta, get_content, put_content

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

def classification():
    	uploaded_files = request.files.getlist("file")
    	app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
    	for file in uploaded_files:
        	filename = secure_filename(file.filename)
        	if filename:
			temp = filename
            		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))	
	
	temp = "/home/ubuntu/FlaskApp/CampusHaat/classification/Test/" + temp	
	model = "/home/ubuntu/FlaskApp/CampusHaat/classification/files/retrained_graph.pb"
	label = "/home/ubuntu/FlaskApp/CampusHaat/classification/files/retrained_labels.txt"
	res =class_run(temp, model, label)
	return jsonify(res)

def canteen_scan():
    	uploaded_files = request.files.getlist("file")
    	app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
    	for file in uploaded_files:
        	filename = secure_filename(file.filename)
        	if filename:
			temp = filename
            		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))	
	
	temp = "/home/ubuntu/FlaskApp/CampusHaat/classification/Test/" + temp	
	res = run(temp)
	return jsonify(res)

def canteen_scan_v():
    	uploaded_files = request.files.getlist("file")
    	app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
    	for file in uploaded_files:
        	filename = secure_filename(file.filename)
        	if filename:
			temp = filename
            		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))	
	
	temp = "/home/ubuntu/FlaskApp/CampusHaat/classification/Test/" + temp	
	res = menu_scanner(temp)
	return jsonify(res)

def price_rec(rating, ip, category):
	impact_fac = {"book":1, "bike":1.6, "cycle":.5}
	pram1 = impact_fac[category]*.15
	pram2 = [.30,.20,.20,.10,.10]
	cp = ip * (1-pram1)
	rp = cp *(1- pram2[rating-1])
	return jsonify(int(rp))

def news_reader(nid):
	content = get_content(nid)
	print content
	name = "/home/ubuntu/FlaskApp/static/audio{0}.mp3".format(nid)
        tta(content, name)
	Directory = "/home/ubuntu/FlaskApp/static/"
	Filename = "audio{0}.mp3".format(nid)
	return send_from_directory(directory=Directory, filename=Filename)

def news_crowler():
	uploaded_files = request.files.getlist("file")
        app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
        for file in uploaded_files:
                filename = secure_filename(file.filename)
                if filename:
                        temp = filename
                        file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))   
	nid = random.randint(1,100000)
        temp = "/home/ubuntu/FlaskApp/CampusHaat/classification/Test/" + temp
	content = "This is a dummy content for testing purpose. "
	content += google_ocr(temp)
	search_term = "Just for testing"
	img_link = "http://ec2-18-191-173-111.us-east-2.compute.amazonaws.com:8000/static/news.png"
	url = "https://satendrapandeymp.github.io/news.html"
	put_content(url, content, nid, img_link, search_term)
        return jsonify({'url':url, "thumb":img_link, "content":content, 'nid':nid})

