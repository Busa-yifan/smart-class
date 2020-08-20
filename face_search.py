# encoding:utf-8
import urllib.request
import json
import base64
import ssl
import CONFIG

'''
人脸搜索
'''
def getresult(pic1path):

    #pic1path = 'G:/tiaozhanbei/baiduapi/checktest/test0.jpg'
    #pic1path = 'G:/tiaozhanbei/baiduapi/test4.jpg'
    f1 = open(pic1path, 'rb')

    pic1 = f1.read()


    img1 = base64.b64encode(pic1)


    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/search"
    context = ssl._create_unverified_context()

    params = json.dumps({"image":str(img1, 'utf-8'),"image_type":"BASE64","group_id_list":"facetest","quality_control":"LOW","liveness_control":"NORMAL"})

    access_token = CONFIG.access_token

    request_url = request_url + "?access_token=" + access_token
    params_2 = params.encode(encoding='UTF8')

    request = urllib.request.Request(url=request_url, data=params_2)

    request.add_header('Content-Type', 'application/json')

    response = urllib.request.urlopen(request,context=context)
    null = ''
    content = response.read()
    content = eval(content)
    result = content['result']
    if(result!=''):
        user_list = result['user_list']
        user_id =  user_list[0]['user_id']
        score =  user_list[0]['score']

        return user_id,score
    else:
        return 0,0


if __name__ == '__main__':
    pic1path = 'G:/tiaozhanbei/baiduapi/test4.jpg'
    result,score = getresult(pic1path)
    print(result,score)

