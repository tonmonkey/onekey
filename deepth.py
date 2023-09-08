# in-deepth query
from main import *
import time

class indeepQuery:
    def __init__(self):
        self.all_indeep_pid_set = set()
        self.indeep_pid_set = set()

    def deepthQuery(self,companyPid_set):
        try:
            for element in companyPid_set.copy():
                self.indeep_pid_set.clear()
                print("\033[1;32m【+】\033[0m" + "正在迭代查询PID:{}下控股公司".format(element))
                # Determine the existence of a holding company
                url = "https://aiqicha.baidu.com/detail/holdsAjax?pid={}&p=1&size=10&confirm=".format(element)
                requests.packages.urllib3.disable_warnings()
                judgeData = requests.get(url=url,headers=header,cookies=cookies,timeout=5,verify=False,proxies=proxies)
                # print(judgeData.text)
                time.sleep(0.5)
                contentLength = judgeData.headers.get('Content-Length')
                print("\033[1;32m【+】\033[0m" + "回包响应大小:{}".format(contentLength))
                if contentLength and int(contentLength)<100:
                    print("\033[0;34m【+】\033[0m" + "PID:{}下无控股公司".format(element))
                else:
                    judgeData_json = json.loads(judgeData.text)
                    judgeTotal = judgeData_json['data']['total']
                    print("\033[0;34m【+】\033[0m" + "PID:{}下控股公司数为:{}".format(element,judgeTotal))
                    print("\033[1;32m【+】\033[0m" + "正在查询中")
                    # page = judgeData_json['data']['pageCount']
                    page = int(judgeTotal/10)+1
                    limit = judgeTotal%10
                    for p in range(1,page+1):
                        if p == page:
                            for n in range(limit):
                                companypid = judgeData_json['data']['list'][n]["pid"]
                                print("\033[1;32m【+】\033[0m" + "控股公司PID为:{}".format(companypid))
                                self.indeep_pid_set.add(companypid)
                                self.all_indeep_pid_set = self.indeep_pid_set
                                # deepth
                                indeepQuery.deepthQuery(self,self.indeep_pid_set)
        except AttributeError as e:
            print(e)

    def outDeepthResult(self):
        for n in self.all_indeep_pid_set:
            print(n)



if __name__ == "__main__":
    companyPid_set = set()
    companyPid_set = {"34299801957255","74011265591181","77794752681209","79701630769171","29942430025317"}
    test = indeepQuery()
    test.deepthQuery(companyPid_set)
    test.outDeepthResult()
