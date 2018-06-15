import urllib2, urllib, os, random, cookielib, time, sys, ssl, HTMLParser
from bs4 import BeautifulSoup as Soup

reload(sys)
sys.setdefaultencoding("utf-8")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Connection': 'keep-alive',}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [headers]




def download(filenames, urls, tags):
	if not os.path.exists("Imgs"):
		os.mkdir("Imgs")
	
	for i in range(len(urls)):
		try:
			url = urls[i]
			tag = str(tags[i])
			filename = "Imgs/" + tag + "/"  + filenames[i]

			if not os.path.exists("Imgs/" + tag):
				os.mkdir("Imgs/" + tag)

			test = opener.open(url, timeout=5)
			with open(filename, 'wb') as file:
				file.write(test.read())
		except:
			print url


seed=raw_input('Meks sure your filename is in this format -: \nurl1\nurl2\n...\nEnter PATH to Filename : ')
file = open(seed, 'r')
result = file.read().split('\n')
filename, urls, tag = [], [], []
for row in result:
	#print row
	try:
		data = row.split("$%")
		for url in data[10].split(";"):
			if url != "":			
				urls.append(url)
				filename.append(data[0])
				tag.append(data[4])
:				print len(data), url
	except:
		print row

download(filename, urls, tag)

