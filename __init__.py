from flask import Flask, request, redirect, session
from views import classification, canteen_scan, canteen_scan_v, price_rec, news_crowler, news_reader

app = Flask(__name__, static_url_path='/static' )
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

@app.route('/price_rec', methods=[ 'GET'])
def pr():
    rating = int(request.args.get('rating'))
    ip = int(request.args.get('mrp'))
    category = request.args.get('cat')
    return price_rec(rating, ip, category)

@app.route('/news', methods=['POST'] )
def news():
    return news_crowler()

@app.route('/news_r', methods=['GET'])
def news_r():
    nid = request.args.get('nid')
    return news_reader(nid)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
