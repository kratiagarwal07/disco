import sys, cv2, time
from utils.ocr_reader import google_ocr_canteen, extract, remover
from scipy import ndimage
from collections import Counter

def run(imagepath):

	start_time = time.time()

	# resizing Image
	image = cv2.imread(imagepath)
	h, w, _ = image.shape
	w = 700.0/w
	h = 900.0/h
	temp = min(w,h)
	temp = cv2.resize(image, (0,0), fx=temp, fy=temp)
	cv2.imwrite(imagepath, temp)

	# sorting result by x, y coordinate of text boxes
	text_result, text_str = google_ocr_canteen(imagepath)
	if len(text_result) < 2:
		return []
	try:
		text_result = sorted(sorted(text_result, key = lambda x : x['y']), key = lambda x : x['x'], reverse = False)
	except:
		return []

	# calculating avg font size
	height = 0
	for temp in text_result:
		height += temp['x'] - temp['x_']

	font_size = height/len(text_result)

	#Adjusting the margin in a row,  Will check if distance is less than font size
	raw_data = [[] for i in range(900)]
	last_row, flag = 0, 0
	for text_box in text_result:
		x = text_box['x']
		if x-last_row < .6 * font_size:
			raw_data[flag].append(text_box)
		else:
			flag = x
			raw_data[flag].append(text_box)
		last_row = x

	final_results = []


	# Real loop for extract everything
	for i in range(900):
		data = raw_data[i]
		if len(data) > 1:
			data = sorted(data, key = lambda x : x['y'])
			# calculating avg font size of the line and avg space
			last = data[0]['y']
			hight = 0
			width = 0
			for temp in data:
				hight += temp['x'] - temp['x_']

			count = 0
			count1 = 1
			for temp in data:
				yl = temp['other']['x']
				y = temp['y']
				temp_width = y-last
				if count in [0,1] and temp_width > 0:
					width += temp_width
					count1 += 1

				elif temp_width < 5 * width/ count1 and temp_width > 0:
					count1 += 1
					width += temp_width

				last = yl
				count += 1

			if count1-2 == 0:
				count1 = 3
			hight = hight/len(data)
			width = width/(count1-2)

			# finally formatting everything as needed
			temp_print_text = ""
			last = data[0]['y']
			for temp in data:
				yl = temp['other']['x']
				y = temp['y']
				if y-last < 4 * width:
					if hight > 1.3 * font_size:
						temp_print_text += " $$" + temp["text"]
					else:
						temp_print_text += "-" + temp["text"]
				else:
					if hight > 1.3*font_size:
						temp_print_text += " $$" + temp["text"]
					else:
						temp_print_text += "&&" + temp["text"]
				last = yl
			final_results.append(temp_print_text[1:])

	first_col = []
	rest = final_results
	title = 'Menu'

	while len(rest) > 1:
		final_results = rest
		rest = []
		for res in final_results:
			if '$$' in res:
				title = res.replace("$$", '')
			elif '&&' in res:
				temp = res.split('&&')
				item_name = temp[0]
				flag, count, price = 0, 1, 0.0
				while(flag == 0 and count < len(temp)):
					num, remaining = extract(temp[count])
					if num == 0.0:
						item_name += temp[count].replace("-", " ")
					else:
						price = num
						flag = 1
					count += 1

				if flag == 1:
					if price < 1000:
						details = {'title':remover(title), 'item_name':remover(item_name), 'price':price}
						first_col.append(details)
					if remaining != "":
						count -= 1
					rest += temp[count:]

				if count < len(temp):
					residue = ""
					left_resudue = temp[count:]
					for element in left_resudue:
						residue += element + "&&"
					rest.append(residue[:-2])
    
	time_taken = str(time.time()-start_time) + " Sec"
	return first_col

if __name__ == '__main__':
	first_col = run(sys.argv[1])
	for data in first_col:
		print data['title'] + "\t" + data['item_name'] + "\t" + str(data['price'])
