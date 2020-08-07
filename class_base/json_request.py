import requests
import json

def logon():
    '''
    请求接口，把服务器返回的响应的数据储存在文件json.md中，
    然后对json.md反序列化处理获取具体的值
    '''
    url = 'http://118.***.***.145:9999/v5/login'
    headers = {
        'Content-Type' : 'application/json;charset = utf-8',
        'Parkingwang-Client-Sourse' : 'ParkingWangAPIClientWeb'
    }
    data = {'username':'','password':''}
    r = requests.post(url,data,headers)
    json.dump(r.json(),open('json.md','w'))

login()
