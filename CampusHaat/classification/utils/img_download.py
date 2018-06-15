import urllib2, urllib, os, random, cookielib, time, sys, ssl, HTMLParser
from bs4 import BeautifulSoup as Soup
import random

reload(sys)
sys.setdefaultencoding("utf-8")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Connection': 'keep-alive',}

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [headers]


def download(url):
	tag = str(random.random())
	filename = "Test/" + tag 

	test = opener.open(url, timeout=5)
	with open(filename, 'wb') as file:
		file.write(test.read())

	return filename
