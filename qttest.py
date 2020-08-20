

import urllib.request
import json
import base64
import ssl

import CONFIG

picf = "G:/tiaozhanbei/facetest/test0.jpg"
f1 = open(picf, 'rb')

pic1 = f1.read()

img1 = base64.b64encode(pic1)

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
context = ssl._create_unverified_context()

params = json.dumps({"image": str(img1, 'utf-8'), "image_type": "BASE64", "face_type": "LIVE"})

access_token = CONFIG.access_token

request_url = request_url + "?access_token=" + access_token

# 转码
params_2 = params.encode(encoding='UTF8')

request = urllib.request.Request(url=request_url, data=params_2)
request.add_header('Content-Type', 'application/json')
response = urllib.request.urlopen(request, context=context)
content = response.read()
null=""
content = eval(content)
print("cotent:", content)
'''
result = content['result']
# print("result:",result)
face_list = result['face_list']
face_num = result['face_num']
# print("face_list:",face_list)
if (face_num != 0):
    location = face_list[0]
    location = location['location']
    height = location['height'];
    left = location['left'];
    top = location['top'];
    width = location['width'];

'''
