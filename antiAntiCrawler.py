# Anti-anti-crawler way
import random
import time

import numpy as np

# 简单的生成随机休眠时间
def randomTime():
    # Set random time
    sleepTime = random.uniform(0.5,4)
    return sleepTime

# 复杂的随机生成修眠时间，使行为更贴近人类动作
def indeepth_randomTime():
    # Get random number
    elements = [0,1,2,3,4,5,6,7,8,9]
    # 设置权值
    weights = [0.05,0.05,0.1,0.1,0.15,0.15,0.15,0.1,0.1,0.05]
    number = np.random.choice(elements, p=weights)
    if number == 0:
        sleepTime = random.uniform(25, 30)
        return sleepTime
    elif number ==1:
        sleepTime = random.uniform(20, 25)
        return sleepTime
    elif number ==2:
        sleepTime = random.uniform(15, 20)
        return sleepTime
    elif number ==3:
        sleepTime = random.uniform(5, 10)
        return sleepTime
    elif number ==4:
        sleepTime = random.uniform(0, 0.5)
        return sleepTime
    elif number ==5:
        sleepTime = random.uniform(0.5, 1)
        return sleepTime
    elif number ==6:
        sleepTime = random.uniform(1.5, 1.7)
        return sleepTime
    elif number ==7:
        sleepTime = random.uniform(1.7, 2.3)
        return sleepTime
    elif number ==8:
        sleepTime = random.uniform(2.3, 5)
        return sleepTime
    elif number ==9:
        sleepTime = random.uniform(10, 15)
        return sleepTime


def randomUa():
    ua_List = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0",
               "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4472.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4472.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.4472.124 Safari/537.36",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.4472.124 Safari/537.36 OPR/77.0.4054.277",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.4472.124 Safari/537.36 Edg/91.0.864.59",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
               ]
    choose = random.randint(0,len(ua_List))
    userAgent = ua_List[choose]
    return userAgent


if __name__ == "__main__":
    for i in range(20):
        a=indeepth_randomTime()
        b=randomUa()
        print(a)
        print(b)
        time.sleep(a)