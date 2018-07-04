import MySQLdb, time
import re, math, re
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    # See which one is more aprropriate for our case and discusse more
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    # sum2 = 1
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def textMatch(num, text):
    conn = MySQLdb.connect(host="35.154.159.250", port=3306, user="admin", passwd="9251640269Guddu", db="campushaat_prod")
    c = conn.cursor()
    cmd = "select AdsId, AdsTitle from ads where AdsCategory={0}".format(num)

    test = c.execute(cmd)
    row = c.fetchall()
    result_title = ""
    result_img = ""
    result_id = 0
    result_score = 0

    text2 = list(set(re.split(' |, |\*|\n|\r', text)))
    #error
    #text2.remove("")

    for i in range(test):
        text1 = row[i][1].lower()
        textId = row[i][0]
	# rid = row[i][1]
	count = 0
	#print(result_score, result_title, result_id)

	# cosine similarity
	vector1 = text_to_vector(text)
	vector2 = text_to_vector(text1)
	score = get_cosine(vector1, vector2)

	# normal similarity
	text3 = re.sub(r'\W+', '', text1)

    	for data in text2:
        	if data in text3:
            		count += 1
            	#print(result_score, result_title, result_id)

    	score = score + (1.0 * count / len(text2))

    	if score > result_score:
        	result_title = text1
        	result_score = score
        	result_id = textId
        #print(result_score, result_title, result_id)

    # result_title=text5
    #print(result_score, result_title, result_id)
    conn.close()
    return result_score, result_title, result_id

def query_final(prod_id):
    conn = MySQLdb.connect(host="35.154.159.250", port=3306, user="admin", passwd="9251640269Guddu", db="campushaat_prod")
    c = conn.cursor()
    cmd = "select AdsCreatedBy, AdsTitle from ads where AdsId={0}".format(prod_id)

    test = c.execute(cmd)
    row = c.fetchone()
    conn.close()
    return row

if __name__ == "__main__":
	result_score, result_title, result_id = textMatch(3, 'thomas')
	print(result_score, result_title, result_id)

# shamelessly copied from stack overflow https://stackoverflow.com/questions/15173225/calculate-cosine-similarity-given-2-sentence-strings
