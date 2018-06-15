from flask import Flask, request, redirect, session
from views import classification, canteen_scan, canteen_scan_v

app = Flask(__name__ )
app.secret_key = "jfjekofeoijfeojifejo"
			
@app.route('/class', methods=[ 'POST'])
def classify():
    return classification()

@app.route('/menu_v', methods=[ 'POST'])
def canteen_v():
    return canteen_scan_v()

@app.route('/menu', methods=[ 'POST'])
def canteen():
    return canteen_scan()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
