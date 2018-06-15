import requests, sys, json
from time import time

def encoding(filename):
    with open(filename, "rb") as f:
        data = f.read()
    return data.encode("base64")

def google_ocr(filename):
    temp = encoding(filename)
    headers = {"Content-Length" : str(len(temp)) , "Content-Type" : "application/json",}
    payload = { "requests": [ {"image": {"content": temp}, "features": [{ "type": "TEXT_DETECTION"}]}]}
    r = requests.post('https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDxxC9U0KQF1aYLepH0icifs49bM6OkKMU', data=json.dumps(payload),  headers=headers, )
    text = r.content
    text = json.loads(text)
    try:
        text = text["responses"][0]["textAnnotations"][0]["description"]
        return text
    except:
        return "No"

def google_ocr_canteen(filename):
    temp = encoding(filename)
    headers = {"Content-Length" : str(len(temp)) , "Content-Type" : "application/json",}
    payload = { "requests": [ {"image": {"content": temp}, "features": [{ "type": "DOCUMENT_TEXT_DETECTION"}]}]}
    r = requests.post('https://vision.googleapis.com/v1/images:annotate?key=AIzaSyDxxC9U0KQF1aYLepH0icifs49bM6OkKMU', data=json.dumps(payload),  headers=headers, )
    text = r.content
    text = json.loads(text)

    text_result = []
    try:
        main_dis = text["responses"][0]["textAnnotations"][0]["description"]
        for i in range(1,len(text["responses"][0]["textAnnotations"])):
            try:
                temp_text = text["responses"][0]["textAnnotations"][i]["description"]
                try:
                    y = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][3]['y']
                except:
                    y = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][2]['y']
                try:
                    x = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][3]['x']
                except:
                    x = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][2]['x']

                try:
                    x_ = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][0]['y']
                except:
                    x_ = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][3]['y']
                other = text["responses"][0]["textAnnotations"][i]["boundingPoly"]["vertices"][2]
                text_result.append({"text":temp_text, "y":x, 'x':y, 'other':other, 'x_':x_})
            except:
                print text["responses"][0]["textAnnotations"][i]
        return text_result, main_dis

    except:
        return [] , ""

def extract(line):
    line = line.strip()
    num = "0"
    rest = ""
    for i in range(len(line)):
        if line[i].isdigit() == True or line[i] == '.':
            num += line[i]
            if line[i] == '.' and '.' in num:
                num = num[:-1*len(line[i])]
        elif float(num) > 0:
            rest = line[i:]
            break
    return float(num), rest

def remover(line):
    line = line.replace("$$", "").replace("-", " ").replace(".", "").replace("&", "")
    line = line.replace("    ", " ").replace("   ", " ").replace("  ", " ")
    line = line.replace("    ", " ").replace("   ", " ").replace("  ", " ")
    line = line.replace("   ", " ").replace("  ", " ").replace("  ", " ")
    temp = line.split(" ")

    try:
        res = temp[0]
        temp.remove('')
    except:
        pass
    for i in range(len(temp)-1):
        if not temp[i][-1].isalpha() or not temp[i+1][0].isalpha():
            res += temp[i+1]
        else:
            res = res + " " + temp[i+1]

    return res + " "
