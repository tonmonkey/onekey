# author: tommonkey

import requests
from config import *
import json
from output import *
import argparse
from deepth import *
from antiAntiCrawler import *


# To get the total subcompany number
def getPage(pid):
    try:
        url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}".format(pid)
        requests.packages.urllib3.disable_warnings()
        rawDate = requests.get(url=url,headers=header,cookies=cookies,timeout=3,verify=False,proxies=proxies)
        rawDate_json = json.loads(rawDate.text)
        # print(rawDate.text)
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
def get_subcompany(number,pid):
    failPage = []
    companyName_list = []
    companyPid_list = []
    page = int(number/10+1)
    limit = int(number%10)
    for p in range(1,page+1):
        try:
            print("\033[1;32m【+】\033[0m"+"正在获取第{}页控股公司".format(p))
            t = randomTime()
            print("\033[1;32m【+】\033[0m"+"休眠因素:{}".format(t))
            time.sleep(t)
            url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}&p={}&size=10&confirm=".format(pid,p)
            rawDate = requests.get(url=url,headers=header,cookies=cookies,timeout=5,verify=False,proxies=proxies)
            rawDate_json = json.loads(rawDate.text)
            # Use re module to get the subcompany name
            print("\033[0;34m【+】\033[0m"+"当前进度:{:.2f}%".format((p/page)*100))
            if p == page:
                for n in range(limit):
                    subcompanyName = rawDate_json['data']['list'][n]["entName"]
                    subcompanypid = rawDate_json['data']['list'][n]["pid"]
                    print("\033[1;32m【+】\033[0m" + "公司名称:{}    公司PID:{}".format(subcompanyName, subcompanypid))
                    companyName_list.append(subcompanyName)
                    companyPid_list.append(subcompanypid)
            else:
                for n in range(10):
                    subcompanyName = rawDate_json['data']['list'][n]["entName"]
                    subcompanypid = rawDate_json['data']['list'][n]["pid"]
                    print("\033[1;32m【+】\033[0m"+"公司名称:{}    公司PID:{}".format(subcompanyName,subcompanypid))
                    companyName_list.append(subcompanyName)
                    companyPid_list.append(subcompanypid)
        except TypeError as e:
            print("\033[5;31;44m【+】\033[0m"+"数据获取失败:失败页数:{}".format(p))
            with open(r'error_log.txt','a+',encoding="utf-8") as errorlog:
                errorlog.write("\033[5;31;44m【+】\033[0m"+"数据获取失败:失败页数:{}\n{}".format(p,rawDate_json))
            failPage.append(p)
            continue
        except IndexError as e:
            print("\033[5;31;44m【+】\033[0m" + "数据获取失败:失败页数:{}".format(p))
            with open(r'error_log.txt', 'a+', encoding="utf-8") as errorlog:
                errorlog.write("\033[5;31;44m【+】\033[0m" + "数据获取失败:失败页数:{}\n{}".format(p, rawDate_json))
            failPage.append(p)
            continue
        print("\033[0;34m【+】\033[0m"+"第{}页控股公司获取成功".format(p))
    print("\033[0;34m【+】\033[0m" + "控股公司爬取完成!")
    return companyName_list,companyPid_list


# Crow all invest company
def get_investcompany(companyName_set,companyPid_set,pid):
    rowData = requests.get(url="https://aiqicha.baidu.com/detail/investajax?p=1&size=10&pid={}".format(pid),headers=header,cookies=cookies,timeout=5,verify=False,proxies=proxies)
    rowData_json = json.loads(rowData.text)
    getTotal = rowData_json['data']['total']
    print("\033[1;32m【+】\033[0m"+"查询投资公司数:{}".format(getTotal))
    getPage = int(getTotal/10+1)
    limit = int(getTotal%10)
    for p in range(1,getPage+1):
        try:
            print("\033[1;32m【+】\033[0m" + "正在获取第{}页投资公司".format(p))
            time.sleep(randomTime())
            url = "https://aiqicha.baidu.com/detail/investajax?p={}&size=10&pid={}".format(p,pid)
            rawDate = requests.get(url=url, headers=header, cookies=cookies, timeout=5, verify=False, proxies=proxies)
            rawDate_json = json.loads(rawDate.text)
            # Use re module to get the invest company name
            if p == getPage:
                for n in range(limit):
                    investcompanyName = rawDate_json['data']['list'][n]["entName"]
                    investcompanypid = rawDate_json['data']['list'][n]["pid"]
                    print("\033[1;32m【+】\033[0m" + "公司名称:{}    公司PID:{}".format(investcompanyName, investcompanypid))
                    companyName_list.append(investcompanyName)
                    companyPid_list.append(investcompanypid)
            else:
                for n in range(10):
                    investcompanyName = rawDate_json['data']['list'][n]["entName"]
                    investcompanypid = rawDate_json['data']['list'][n]["pid"]
                    print("\033[1;32m【+】\033[0m" + "公司名称:{}    公司PID:{}".format(investcompanyName, investcompanypid))
                    companyName_list.append(investcompanyName)
                    companyPid_list.append(investcompanypid)
            print("\033[0;34m【+】\033[0m" + "第{}页投资公司获取成功".format(p))
        except TypeError as e:
            print("\033[5;31;44m【+】\033[0m"+"数据获取失败:失败页数:{}".format(p))
            with open(r'error_log.txt','a+',encoding="utf-8") as errorlog:
                errorlog.write("\033[5;31;44m【+】\033[0m"+"数据获取失败:失败页数:{}\n{}".format(p,rawDate_json))
            # failPage.append(p)
            continue
        except IndexError as e:
            print("\033[5;31;44m【+】\033[0m" + "数据获取失败:失败页数:{}".format(p))
            with open(r'error_log.txt', 'a+', encoding="utf-8") as errorlog:
                errorlog.write("\033[5;31;44m【+】\033[0m" + "数据获取失败:失败页数:{}\n{}".format(p, rawDate_json))
            # failPage.append(p)
            continue
    print("\033[0;34m【+】\033[0m" + "投资公司爬取完成!")
    return companyName_list, companyPid_list

# Pid to company
def pid_to_Company(pid_list):
    company_list = []
    for p in pid_list:
        time.sleep(randomTime())
        url = "https://aiqicha.baidu.com/relations/doubtControllerAjax?pid={}".format(p)
        rowData = requests.get(url=url, headers=header, cookies=cookies, timeout=5, verify=False, proxies=proxies)
        rawData_json = json.loads(rowData.text)
        companyName = rawData_json['data']['compName']
        print(companyName)
        company_list.append(companyName)
    return company_list

# Add args
def args_deal():
    parse = argparse.ArgumentParser(prog="OneKey-QACQ", description='''\033[5;31;44m1.python3 main.py -h2.python3 main.py -m a\033[0m''')
    parse.add_argument("-m", "--module",action="store", help="Mode choose:1.-m a    2.-m d")
    opt = parse.parse_args()
    return opt


if __name__ == "__main__":
    print(banner)
    args = args_deal()
    if args.module=="a":
        number = getPage(pid)
        companyName_list, companyPid_list = get_subcompany(number,pid)
        companyName_list, companyPid_list = get_investcompany(companyName_list,companyPid_list,pid)
        dealDate(companyName_list, companyPid_list)
    elif args.module=="d":
        pid_list = []
        companyPid_list = []
        main_companyPid = InPid

        Indeepth_Obj = indeepQuery()
        Indeepth_Obj.deepthQuery(main_companyPid)
        pid_list = Indeepth_Obj.outDeal_Pid()
        company_list = pid_to_Company(pid_list)
        dealDate(company_list, pid_list)
    else:
        print("\033[5;31;44m【+】\033[0m"+"运行异常:请输入正常参数")