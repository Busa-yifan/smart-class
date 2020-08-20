import urllib3
import base64
import json
import CONFIG

def getresult(pic1path,pic2path):

    f1 = open(pic1path, 'rb')
    f2 = open(pic2path, 'rb')
    pic1 = f1.read()
    pic2 = f2.read()

    access_token = CONFIG.access_token
    http=urllib3.PoolManager()
    IMAGE_TYPE='BASE64'

    url='https://aip.baidubce.com/rest/2.0/face/v3/match?access_token='+access_token


    #参数image：图像base64编码 分别base64编码后的2张图片数据

    img1 = base64.b64encode(pic1)
    img2 = base64.b64encode(pic2)

    #params = {"images":str(img1,'utf-8') + ',' + str(img2,'utf-8')}

    params = [{"image":str(img1,'utf-8'),"image_type":IMAGE_TYPE},{"image":str(img2,'utf-8'),"image_type":IMAGE_TYPE}]
    #参数转JSON格式

    encoded_data = json.dumps(params).encode('utf-8')
    request=http.request('POST',
                          url,
                          body=encoded_data,
                          headers={'Content-Type':'application/json'})
    #对返回的byte字节进行处理。Python3输出位串，而不是可读的字符串，需要进行转换
    result = str(request.data)
    result_sp = result.split('"')[16]
    face_score = result_sp[1:-1]
    return(float(face_score))