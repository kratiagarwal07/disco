from flask import Flask, render_template, request, send_from_directory, redirect, current_app,  session, jsonify
import os, sys, subprocess
from werkzeug import secure_filename
from class_testing import class_run
from menu_scan_branch import run
from menu_scan import menu_scanner


reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = '/mnt/storage/Others/'


def classification():
    	uploaded_files = request.files.getlist("file")
    	app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
    	for file in uploaded_files:
        	filename = secure_filename(file.filename)
        	if filename:
			temp = filename
            		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))	
	
	temp = "/home/intel/FlaskApp/CampusHaat/classification/Test/" + temp	
	model = "/home/intel/FlaskApp/CampusHaat/classification/files/retrained_graph.pb"
	label = "/home/intel/FlaskApp/CampusHaat/classification/files/retrained_labels.txt"
	res = class_run(temp, model, label)
	return jsonify(res)

def canteen_scan():
    	uploaded_files = request.files.getlist("file")
    	app.config['DOWNLOAD_FOLDER'] = "CampusHaat/classification/Test/"
    	for file in uploaded_files:
        	filename = secure_filename(file.filename)
        	if filename:
			temp = filename
            		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))	
	
	temp = "/home/intel/FlaskApp/CampusHaat/classification/Test/" + temp	
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
	
	temp = "/home/intel/FlaskApp/CampusHaat/classification/Test/" + temp	
	res = menu_scanner(temp)
	return jsonify(res)

