import requests, sys, json
from time import time

time1 = time()

def encoding(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data.encode("base64")


def google_search(name, key="AIzaSyBYEALDuG5nJAING453cY7sCIoaeutDR-4"):
    headers = {"Content-Type" : "application/json",}
    name.replace("'", "")
    name.replace('"', "")
    #name = "+".join(name.split(" "))
    #payload = { "requests": [ {"image": {"content": temp}, "features": [{ "type": "TEXT_DETECTION"}]}]}
    #https://www.googleapis.com/demo/v1?key=YOUR-API-KEY&fields=kind,items(title,characteristics/length)
    uri = "https://www.googleapis.com/customsearch/v1?key=" + key + "&cx=003324795964724942257:5nqvkeopayi&num=5&fields=items(title,link)&q=" + name
    r = requests.get(uri, headers=headers, )
    text = r.content
    text = json.loads(text)
    print text
    titles = []
    links = []
    try:
        for i in range(len(text["items"])):
            try:
                titles.append((text["items"][i]["title"]))
                links.append((text["items"][i]["link"]))
            except:
                print links
                return []
    except:
        pass
    return links

if __name__ == "__main__":
    print google_search("gst, rate cut, fpi return figure on 2016 market wishlist")
    print time() - time1
