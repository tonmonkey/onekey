import json
from config import *
import requests
import time
from output import *


# Gets the total number of holding companies
def get_page(id):
    url = "https://aiqicha.baidu.com/compdata/navigationListAjax?pid={}".format(id)
    get_hold = requests.get(url=url, headers=header,timeout=5,verify=False)
    get_hold_json = json.loads(get_hold.text)
    get_hold_value = get_hold_json['data'][0]['children'][10]['total']
    page = int(get_hold_value/10)+1
    print("Get the total number of holding companies: {}".format(get_hold_value))
    return page


# Query the data
def get_date(id,page):
    try:
        for i in range(1,page):
            url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}&p={}&size=10&confirm=".format(id,i)
            respond = requests.get(url=url,headers=header,timeout=8,verify=False)
            time.sleep(2)    # control time
            respond_json = json.loads(respond.text)
            for n in range(0,10):
                companyUnicodeName = respond_json['data']['list'][n]['entName']
                input_data(companyUnicodeName)
                print("Crawl page {}, article {} is completed, and successfully put into storage".format(i,n))
    except Exception as err:
        print(err)