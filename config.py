# banner
banner = """


  ____   ___   ______   __
 / __ \ / _ \ / __ \ \ / /
| |__| | |_| | |__| \ v / 
|  __  |  _  |  __  |> <  
| |__| | | | | |__| / ^ \ 
 \____/|_| |_|\____/_/ \_\


blog:https://www.tommonkey.cn
"""

# 这里的cookie自己用bp抓取替换就ok了
header={
'Cookie':'_j47_ka8_=57; log_guid=8d6434ed395f772a4f54e4364025649d; BDUSS=0t-UzdnUzRvcHRVNmM4VHdIZEZ3QVJUb3p4VTdwZnFuMzY5bnZhaU1CNThFeHhrRUFBQUFBJCQAAAAAAAAAAAEAAABYHnlpzOzQ0L~VwNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHyG9GN8hvRjS; BDUSS_BFESS=0t-UzdnUzRvcHRVNmM4VHdIZEZ3QVJUb3p4VTdwZnFuMzY5bnZhaU1CNThFeHhrRUFBQUFBJCQAAAAAAAAAAAEAAABYHnlpzOzQ0L~VwNYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHyG9GN8hvRjS; BDPPN=2360f3ee55bc92ec4eaeb23093ef08f2; _t4z_qc8_=xlTM-TogKuTw04S3lOvLO3LntB3WQm43xwmd; BAIDUID=ACBBC6E4D4DD00732E10932608200FC1:FG=1; BIDUPSID=ACBBC6E4D4DD00732E10932608200FC1; PSTM=1678330391; MCITY=-%3A; Hm_lvt_ad52b306e1ae4557f5d3534cce8f8bbf=1685148364; BDSFRCVID=uH4OJeC62Gzs2MOff21SUJ_ck2K5xkRTH6_nTqRUQtuVblHNFMEIEG0PHf8g0KubM9-MogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbFt_DtbJIK3HR7pK4OVMJvH-UIsKU4OB2Q-5KL-fRjrHpo_b67GMMkIXfTzXPQiJ6bWbfbdJf7_Ol5NhjJaqfrbKn7rJtc9bgTxoUJPQCnJhhvGXfOBQnkebPRiWTj9QgbLMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0hC-CDT05D6cM5pJfeJOHaK7-Q-OOajrjDnCrXqJrXUI8LNDH2R3QBabN0Dnl2UbY8JrLWM7s0pQL3bO7tqRXJavh3lTw5qFVJlr8QxcpyfL1Db37KjvMtg3t3qCXHl6oepvoX55c3MkDBPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtbPt_DI2JCt3fJrYhPIV-PAt-U4Xat0XKKOLV-jx0h7keq8CD6JZQxIf0xj9LbQOBmjXhfnF55C-hq72y5jrh4TDQxnjJqJ4MDvyVlrn3UQpsIJM3q_WbT8UQ4FOtP7ZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe63WjNKtt5_8fKrBstc_2DL-bDIk-PnVeUPv0-nZKxtqtD5UbC3q-JQ4SqR1Xfcl344mh4OqWTJnWncdWJ_EBxQOs4QsDDcayf__2RO405OT-IFO0KJc0l6Ks-nqhPJvyU7XXnO72lRlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtIFtVD_2JD82hI_wenJb5ICQKxn2KRJeaK_X3b7Ef-51Mh7_bf--Dx-hKN5uW-5htJ6g-lc7KbkKOI59Mp5xy5KmhRODQqQIbTTp3JRdBqQYsqTHQT3my-5bbN3i-4juf4juWb3cWh4K8UbShJoPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uJtJADoMK; H_PS_PSSID=38515_36549_38687_38673_38796_38767_38579_38485_38816_38821_38638_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=0g8k2ka12k2l018kak2k001o1i7qsqs1n; delPer=0; PSINO=5; ZFY=jP05pC13QWtFATh0obLHejwK5UQHSfK33VavsOPy0BU:C; BAIDUID_BFESS=ACBBC6E4D4DD00732E10932608200FC1:FG=1; BDSFRCVID_BFESS=uH4OJeC62Gzs2MOff21SUJ_ck2K5xkRTH6_nTqRUQtuVblHNFMEIEG0PHf8g0KubM9-MogKKL2OTHmuF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbFt_DtbJIK3HR7pK4OVMJvH-UIsKU4OB2Q-5KL-fRjrHpo_b67GMMkIXfTzXPQiJ6bWbfbdJf7_Ol5NhjJaqfrbKn7rJtc9bgTxoUJPQCnJhhvGXfOBQnkebPRiWTj9QgbLMhQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0M5DK0hC-CDT05D6cM5pJfeJOHaK7-Q-OOajrjDnCrXqJrXUI8LNDH2R3QBabN0Dnl2UbY8JrLWM7s0pQL3bO7tqRXJavh3lTw5qFVJlr8QxcpyfL1Db37KjvMtg3t3qCXHl6oepvoX55c3MkDBPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtbPt_DI2JCt3fJrYhPIV-PAt-U4Xat0XKKOLV-jx0h7keq8CD6JZQxIf0xj9LbQOBmjXhfnF55C-hq72y5jrh4TDQxnjJqJ4MDvyVlrn3UQpsIJM3q_WbT8UQ4FOtP7ZaKviah4-BMb1Df7DBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTD-Dhe63WjNKtt5_8fKrBstc_2DL-bDIk-PnVeUPv0-nZKxtqtD5UbC3q-JQ4SqR1Xfcl344mh4OqWTJnWncdWJ_EBxQOs4QsDDcayf__2RO405OT-IFO0KJc0l6Ks-nqhPJvyU7XXnO72lRlXbrtXp7_2J0WStbKy4oTjxL1Db3JKjvMtIFtVD_2JD82hI_wenJb5ICQKxn2KRJeaK_X3b7Ef-51Mh7_bf--Dx-hKN5uW-5htJ6g-lc7KbkKOI59Mp5xy5KmhRODQqQIbTTp3JRdBqQYsqTHQT3my-5bbN3i-4juf4juWb3cWh4K8UbShJoPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JDMr0exbH55uJtJADoMK; log_first_time=1685946249554; _fb537_=xlTM-TogKuTwKFvlYDQrVl4gf3z20dHfC861qDQj7VcdTZ7QEwCULmwmd; Hm_lpvt_ad52b306e1ae4557f5d3534cce8f8bbf=1685946282; ab_sr=1.0.1_NzBmODMyZGY5NDNkNzc3MzNlZjdkNzUwZjEzYjhmM2U5NzdlYzcyMzM4YjYwNDUzZTkxYjJjNzY3MmJlMjViNzRmZDMyOTM5NjMxOWRhZDhmZjYyYzg5MGJjZWRmNDRlMjBiYTU5MjUxYTE5ODk2ODc3MzFhZmY3ZmEwZGM1YjEzZjA2Mzk1OTk1NDNhNjc3YWE4MzdjYTU1NDkwMDUwNzA1N2Q1MTRmM2FjMThjMDE0Y2FkNGE2NjM3MzYyMWJkYWMwMGRiYWYxMzhiNTM0M2M0ZjkwY2JjNzc0OGJkZjA=; _s53_d91_=517a080608b8bd9031261d9ecb8deb705d0aa1f05c0e571fd71a5742fe31800601dd6bb50ca0025e1a0c4dfd6072d6ec1c4358e04b929f9367758eb56bd11110007e3479a112d7cdd4f083471d58c314eb09832b9aa780730192e30024f68940d3504f5653ee4236c16c02980d76705cc123d9e11152a96122c32f4dd582ae1668273212612ff6dda860b9009d743f6891732b8cfaacef8c9b80e56cc274418d10f7f5b5b69bf540fca49252c374c7b325ae68fbd841820f5109c0584a27e366115eb2ce010d7b448861a1ded5ab0b0c46fac958900a498bf0bd66dadf6ba3273109c5a172fdc4ea92e2e67a27665c50; _y18_s21_=bb4a2356; log_last_time=1685946294318; RT="z=1&dm=baidu.com&si=e0776b95-b71c-4117-8c04-12eed5c45c8d&ss=liigv5s5&sl=3&tt=98g&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf"; ab168594480=791190167f45c87b24bf7b5c797a2d2116859462949c1',
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