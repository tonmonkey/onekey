import sys
import time
from urllib.parse import unquote
import requests
from config import *
import json
from output import *


# To get the total subcompany number
def getPage(pid):
    try:
        url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}".format(pid)
        requests.packages.urllib3.disable_warnings()
        rawDate = requests.get(url=url,headers=header,cookies=cookies,timeout=3,verify=False,proxies=proxies)
        rawDate_json = json.loads(rawDate.text)
        # get the value of page
        number = rawDate_json['data']['total']
        if rawDate.status_code == 200 and number is not None:
            print("\033[1;32m【+】\033[0m"+"查询控股公司数:{}".format(number))
            return number
        else:
            print("\033[5;31;44m【+】\033[0m"+"获取控股公司数量失败!请检查网络")
    except Exception as err:
        print("\033[5;31;44m【+】\033[0m"+"运行异常:",err,"报错模块:getPage()")



# Crow all subcompany
def get_date(number,pid):
    companyName_set = set()
    companyPid_set = set()
    page = int(number/10+1)
    limit = int(number%10)
    for p in range(1,page+1):
        print("\033[1;32m【+】\033[0m"+"正在获取第{}页控股公司".format(p))
        url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}&p={}&size=10&confirm=".format(pid,p)
        rawDate = requests.get(url=url,headers=header,cookies=cookies,timeout=5,verify=False,proxies=proxies)
        rawDate_json = json.loads(rawDate.text)
        # Use re module to get the subcompany name
        if p == page:
            for n in range(limit):
                subcompanyName = rawDate_json['data']['list'][n]["entName"]
                subcompanypid = rawDate_json['data']['list'][n]["pid"]
                print("\033[1;32m【+】\033[0m" + "公司名称:{}    公司PID:{}".format(subcompanyName, subcompanypid))
                companyName_set.add(subcompanyName)
                companyPid_set.add(subcompanypid)
        else:
            for n in range(10):
                subcompanyName = rawDate_json['data']['list'][n]["entName"]
                subcompanypid = rawDate_json['data']['list'][n]["pid"]
                print("\033[1;32m【+】\033[0m"+"公司名称:{}    公司PID:{}".format(subcompanyName,subcompanypid))
                companyName_set.add(subcompanyName)
                companyPid_set.add(subcompanypid)
        print("\033[0;34m【+】\033[0m"+"第{}页控股公司获取成功".format(p))
    print("\033[0;34m【+】\033[0m" + "控股公司爬取完成!")
    return companyName_set,companyPid_set

if __name__ == "__main__":
    print(banner)
    number = getPage(pid)
    companyName_set,companyPid_set = get_date(number,pid)
    dealDate(companyName_set,companyPid_set)

