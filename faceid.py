# encoding:utf-8
import urllib.request
import json
import base64
import ssl
import CONFIG

def getresult(pic1path,pic2path):
    f1 = open(pic1path, 'rb')
    f2 = open(pic2path, 'rb')
    pic1 = f1.read()
    pic2 = f2.read()

    img1 = base64.b64encode(pic1)
    img2 = base64.b64encode(pic2)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    context = ssl._create_unverified_context()

    params = json.dumps(
        [{"image": str(img1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"},
         {"image": str(img2, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE", "quality_control": "LOW"}])

    access_token = CONFIG.access_token
    request_url = request_url + "?access_token=" + access_token
    #转码
    params_2 = params.encode(encoding='UTF8')

    request = urllib.request.Request(url=request_url, data=params_2)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request,context=context)
    content = response.read()
    content = eval(content)
    score = content['result']['score']
    return(score)

