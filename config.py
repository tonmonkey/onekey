# config file
# banner
banner = """
OneKey
 .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. |
| |    ___       | | |      __      | | |    ___       | | |     ______   | |
| |  .'   '.     | | |     /  \     | | |  .'   '.     | | |   .' ___  |  | |
| | /  .-.  \    | | |    / /\ \    | | | /  .-.  \    | | |  / .'   \_|  | |
| | | |   | |    | | |   / ____ \   | | | | |   | |    | | |  | |         | |
| | \  `-'  \_   | | | _/ /    \ \_ | | | \  `-'  \_   | | |  \ `.___.'\  | |
| |  `.___.\__|  | | ||____|  |____|| | |  `.___.\__|  | | |   `._____.'  | |
| |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' 
Version 0.2.2                                          ----Author:tommonkey
"""

# setting proxy
proxies = {
    'http': 'http://localhost:7890',
    'https': 'http://localhost:7890'
}


# setting company PID
# Normal mode query.查询单个目标，耗时少，速度快
pid = 000000000
# In-deepth mode query.可查询单个或多个目标，耗时长，速度慢，发包量巨大，但覆盖面广，结果数量多
InPid = {"000000000",}


# setting Cookie
cookies = {'Cookie':''}
# setting head
header={
'Sec-Ch-Ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
'Sec-Ch-Ua-Mobile':'?0',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
'Accept':'application/json, text/plain, */*',
'Ymg_ssr':'1668755050538_1668842314729_newx3Oy/bZS3JmKFpuSXF0dFO4LitarO41oOAYMKwim4cWMEziXdEuJoQqC9Po8LnWo5xdt5QyC5SUq0hbg09nAW2K1O1NLJfYLrz3r5165KX/7gQEiIR50kz9mBZl08hCunvgRxyRAAwMXTzf25rjN4BpVmunVEUgBmHGR2d5nht+Vzq1QbtBcEwic4HqBWMMGj90dLwILVd0tapplxu4J2lRAgEpW1yLNHPdgmYCA1BS4urb1LmCaUDTC7I8ToSDsexLbmlVuYoOmx+4IlzdZGWV51fl9B7gAktxPdg5qra2UZ9Y57+gJypVJXOtNgJRSL3JjP7XDgYo8bUtTEA6/4vTTYBJLA4CBJ7oXStz8=',
'X-Requested-With':'XMLHttpRequest',
'Zx-Open-Url':'https://aiqicha.baidu.com/company_detail_28684316400936',
'Sec-Ch-Ua-Platform':'Windows',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Dest':'empty',
'Referer':'https://aiqicha.baidu.com/company_detail_28684316400936',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7',
'Connection':'close',
}