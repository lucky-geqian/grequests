# -*- coding: utf8 -*-
import datetime
import requests
import hashlib
import json
import time
import sys
# -*- coding: utf8 -*-
import datetime
import requests
import hashlib
import json
import time
import sys
import grequests


def main():
    # path = argv[1]
    # data_part = datetime.datetime.today().strftime('_%Y%m%d_%H%M')
    # output_path = path.replace(".csv", "_" + data_part + ".out", 1)
    # file = open(path, "r")
    # lines = file.read().splitlines()
    # writer = open(output_path, 'w')

    a = ['你好', '再见', '后会有期']
    b_url = ['0', '0']
    response = ['0', '0']
    httpsession = requests.session()

    # for i in range(1, 1000):
    #     r = httpsession.post("https://www.oschina.net/test?query=%s" % i)
    #     print(r)
    time1 = time.time()
    for i in range(len(a)):
        r = httpsession.get("http://aisapi.n.shifen.com:8200/beta/nlu/api/v1/94e9e6ae-da31-4a95-ba72-c46696f9cf28?token=Sx2k2o8e1ToNP9yBAG6lRmpCY1J4glQp&q=%r" % i)
        time3 = time.time()
        print(str(time3 - time1))
        print(r.json())
        # b_url[i] = baidu_url(a[i])

        # response['msg'] = line

    # rs = (grequests.get(u) for u in b_url)
    time2 = time.time()
    # grequests.map(rs, exception_handler=exception_handler)
    print(str(time2 - time1))
    # grequests.map(rs)
    #     print(str(time2-time1))
    #     print(response.json())
    #     writer.write(line + "*" + str(response.json()['intents'][0]['intent']) + "\n")
    #
    # writer.close()

def baidu_url(line):
    return 'http://aisapi.n.shifen.com:8200/beta/nlu/api/v1/94e9e6ae-da31-4a95-ba72-c46696f9cf28?token=Sx2k2o8e1ToNP9yBAG6lRmpCY1J4glQp&q=%r' % line




if  __name__ =='__main__':
    main()


# def main():
#     # path = argv[1]
#     # data_part = datetime.datetime.today().strftime('_%Y%m%d_%H%M')
#     # output_path = path.replace(".csv", "_" + data_part + ".out", 1)
#     # file = open(path, "r")
#     # lines = file.read().splitlines()
#     # writer = open(output_path, 'w')
#
#     a = ['你好', '再见']
#     b_url = ['0', '0']
#     response = ['0', '0']
#     for i in range(len(a)):
#         time1 = time.time()
#         b_url[i] = baidu_url(a[i])
#         time2 = time.time()
#         # response['msg'] = line
#     rs = (grequests.get(u) for u in b_url)
#     # grequests.map(rs, exception_handler=exception_handler)
#     for num in rs:
#         print(num)
#     # grequests.map(rs)
#     #     print(str(time2-time1))
#     #     print(response.json())
#     #     writer.write(line + "*" + str(response.json()['intents'][0]['intent']) + "\n")
#     #
#     # writer.close()

def baidu_url(line):
    return 'http://aisapi.n.shifen.com:8200/beta/nlu/api/v1/94e9e6ae-da31-4a95-ba72-c46696f9cf28?token=Sx2k2o8e1ToNP9yBAG6lRmpCY1J4glQp&q=%r' % line

