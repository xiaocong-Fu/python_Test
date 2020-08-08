import requests
import urllib3
import json

# def logon():
#     '''
#     请求接口，把服务器返回的响应的数据储存在文件json.md中，
#     然后对json.md反序列化处理获取具体的值
#     '''
#     url = 'http://118.***.***.145:9999/v5/login'
#     headers = {
#         'Content-Type' : 'application/json;charset = utf-8',
#         'Parkingwang-Client-Sourse' : 'ParkingWangAPIClientWeb'
#     }
#     data = {'username':'','password':''}
#     r = requests.post(url,data,headers)
#     json.dump(r.json(),open('json.md','w'))
#
# login()

# ---------------------------------------------------------json库实例------------------------------------------------------
# 1.拉钩网搜索(可以正常发送请求，但是返回“操作太快”的提示)
def headers():
    headers = {
        'Content-Type':'application/json;charset=utf-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 84.0.4147.105 Safari/537.36',
        'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
        'Cookie':'_ga = GA1.2.767306751.1596856240;'
                 'user_trace_token=20200808111042-9b90067d-def6-413f-a1e8-5f5086008101;'
                 'LGUID=20200808111043-55e287ff-875d-46ff-815c-cee2a7d09b4f;'
                 'index_location_city=%E5%8C%97%E4%BA%AC;'
                 'JSESSIONID=ABAAABAABAGABFA707DA95352023C1C43E9A15B03CCAA00; _gat = 1;'
                 '_gid=GA1.2.31755732.1596856528;'
                 'LGSID=20200808111043-30c62cb2-db91-4598-ab31-fb922d4b4b0b;'
                 'PRE_UTM=m_cf_cpc_baidu_pc;'
                 'PRE_HOST=www.baidu.com;'
                 'PRE_SITE=;'
                 'PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm%5Fsource%3Dm%5Fcf%5Fcpc%5Fbaidu%5Fpc%26m%5Fkw%3Dbaidu%5Fcpc%5Fbj%5Fadc5f4%5F94c1f8%5F%253B%25E6%258B%2589%25E9%2592%25A9%26bd%5Fvid%3D8670254561058776145;'
                 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1596856240;'
                 'SEARCH_ID=139d9ce160e34f07a5e6718145976ee6;'
                 'LGRID=20200808111619-bbff2682-0a1f-4386-90d7-7ed809244fc1;'
                 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1596856576;'
                 'TG-TRACK-CODE=index_search'
    }
    return headers

def laGou():
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=False'    # positionAjax.json?needAddtionalResult=False
    data = {'first':'False','pn':1,'kd':'自动化测试工程师'}
    header = headers()
    r = requests.post(url,data,header)
    json.dump(r.json(),open('lagou.json','w'))

def dataAndlysis():
    positions = []
    datas = json.load(open('lagou.json','r'))
    # 获取名称，职位
    for data_key , data_value in datas.items():
        company = str(data_key) + '----' + str(data_value)
        print(company)


laGou()
dataAndlysis()