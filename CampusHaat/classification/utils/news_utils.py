from gtts import gTTS
import MySQLdb, time

def get_content(nid):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="Guddu_Bro", db="news")
    c = conn.cursor()
    cmd = "select content from news_details where nid={0}".format(nid)
    test = c.execute(cmd)
    content = ""
    conn.close()
    if test > 0:
	content = c.fetchone()[0]
    return content

def put_content(url, content, nid, img_link, search_term):
    conn = MySQLdb.connect(host="localhost", user="root", passwd="Guddu_Bro", db="news")
    c = conn.cursor()
    cmd = "INSERT INTO news_details (url, content, nid, img_link, search_term) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(url, content, nid, img_link, search_term )
    test = c.execute(cmd)
    conn.commit()
    conn.close()

def tta(data, name):
    tts = gTTS(text=data , lang='hi')
    tts.save(name)

