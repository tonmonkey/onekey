# in-deepth query
import time
import requests
from config import *
import json
from antiAntiCrawler import *

class indeepQuery:
    def __init__(self):
        self.indeep_pid_list = []
        self.store_List = []

    def dealSet(self,store_set):
        self.store_List.append(store_set)

    def outDeal_Pid(self):
        # for i in self.store_List:
        #     print(i)
        return self.store_List

    def deepthQuery(self,companyPid):
        store_list = []
        try:
            for e in companyPid:
                print("\033[1;32m【+】\033[0m" + "正在迭代查询PID:{}下控股公司".format(e))
                # Determine the existence of a holding company
                url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}&p=1&size=10&confirm=".format(e)
                requests.packages.urllib3.disable_warnings()
                judgeData = requests.get(url=url,headers=header,cookies=cookies,timeout=5,verify=False,proxies=proxies)
                # print(judgeData.text)
                t = randomTime()
                print("\033[1;32m【+】\033[0m" + "休眠因素:{}".format(t))
                time.sleep(t)
                contentLength = judgeData.headers.get('Content-Length')
                print("\033[1;32m【+】\033[0m" + "回包响应大小:{}".format(contentLength))
                if contentLength and int(contentLength)<100:
                    print("\033[0;34m【+】\033[0m" + "PID:{}下无控股公司".format(e))
                else:
                    judgeData_json = json.loads(judgeData.text)
                    judgeTotal = judgeData_json['data']['total']
                    print("\033[0;34m【+】\033[0m" + "PID:{}下控股公司数为:{}".format(e,judgeTotal))
                    print("\033[1;32m【+】\033[0m" + "正在查询中")
                    # page = judgeData_json['data']['pageCount']
                    page = int(judgeTotal/10)+1
                    limit = judgeTotal%10
                    for p in range(1,page+1):
                        if p == page:
                            for n in range(limit):
                                nextCompanypid = judgeData_json['data']['list'][n]["pid"]
                                print("\033[1;32m【+】\033[0m" + "控股公司PID为:{}".format(nextCompanypid))
                                self.indeep_pid_list.append(nextCompanypid)
                                # deepth
                                indeepQuery.deepthQuery(self,nextCompanypid)
                        else:
                            for n in range(10):
                                nextCompanypid = judgeData_json['data']['list'][n]["pid"]
                                print("\033[1;32m【+】\033[0m" + "控股公司PID为:{}".format(nextCompanypid))
                                self.indeep_pid_list.append(nextCompanypid)
                                # deepth
                                indeepQuery.deepthQuery(self,nextCompanypid)
        except AttributeError as e:
            print(e)


# if __name__ == "__main__":
#     companyPid_set = set()
#     companyPid_set = {"1234567890"}
#     test = indeepQuery()
#     test.deepthQuery(companyPid_set)
#     pid_list = test.outDeal_Pid()