import urllib2, urllib, os, random, cookielib, time, sys, ssl, HTMLParser
from bs4 import BeautifulSoup as Soup
from selenium import webdriver

# list to find useful section
parse_list = ['story-details', 'story-section', 'story-content', 'article-body section', 'article-section', 'article-full-content' ]

# Making utf-8 default encoding
reload(sys)
sys.setdefaultencoding("utf-8")

# Avoiding SSL problems
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# creating headers
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Connection': 'keep-alive',}

# creating build_opener
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPSHandler(context=ctx), urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [headers]

# loading selenium build_opener
for key in headers:
    webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]
browser = webdriver.PhantomJS()

# fetch news from google
def google_links(page):
    res = []
    browser.get(page)
    time.sleep(2)
    Page_Html = browser.page_source

    '''
    with open("temp.html", 'w') as file:
        file.write(Page_Html)
    '''

    Parsed_html = Soup(Page_Html, "html.parser")
    Container = Parsed_html.findAll("div", {"id":"rso"})[0]
    rows = Container.findAll("div", {"class":"g"})

    for row in rows:
	try:
	    link = row.findAll("a")[0]['href']
	    original = link
	    link = link.replace("%3A", ":")
	    link = link.replace("%2F", "/")
	    link = link.replace("%2520", "%20")
	    res.append(link)
	except:
	    print "Found something not captured"

    return res


def download(name, arr, num):
	count = 0
	for doc in arr:
	    count += 1
	    link = doc
	    filename = link.split("://")[1].split("/")[0]
	    news_agency = filename
	    filename = filename + "_" + str(random.randint(1,9999)) + ".html"
	    try:
		test = opener.open(link, timeout=5)
		Page_Html = test.read()
		Parsed_html = Soup(Page_Html, "html.parser")
		title = Parsed_html.findAll("h1")[0].text
		for elem in parse_list:

		    try:
			Container = Parsed_html.findAll("div", {"class":elem})[0]
			print "Sucessfull now"
			Page_Html = Container
			with open(filename, 'w') as wr:
				wr.write("Title: " + title + " \n\n" + str(Page_Html))
			break

		    except:
			continue
		     
	    except:
		    print link
	    
	    if count > num:
		break

seed=raw_input('Enter the keywords : ')
#num=int(raw_input('No of News you want -- : '))
num = 1
query = "https://www.google.co.in/search?num=100&client=ubuntu&hs=RWy&channel=fs&dcr=0&source=lnms&tbm=nws&sa=X&ved=0ahUKEwjAr5-vjcHZAhUMsI8KHe_3DSkQ_AUICigB&biw=1366&bih=662&q=" + "+".join(seed.split(' '))
result = google_links(query)
download(seed, result, num)
os.remove("ghostdriver.log")

