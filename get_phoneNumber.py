# -*- coding: utf-8 -*-

import requests
import re
import csv
import time
from crawl_ip import IPUtil

def getURL(name, proxies=None):

    try:
        webURL = r'https://m.qichacha.com/search?key={}'.format(name)
        # webURL = r'http://m.qichacha.com/search'

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'UM_distinctid=165f1c66f91405-090576f8c1764-1130685c-1aeaa0-165f1c66f92680; zg_did=%7B%22did%22%3A%20%22165f1c66fab1aa-0c33c8fd0a5598-1130685c-1aeaa0-165f1c66fac7be%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1537359639,1537416930; _uab_collina=153741693062669146646239; acw_tc=9dff284115374169353944389e736c286ff8760092823790059c8da7d4; PHPSESSID=3008u9r2drm3q5ofn9kh68gmt0; QCCSESSID=3k4805qvhmb5h9e1bhs7k673e3; CNZZDATA1254842228=539091877-1537413217-https%253A%252F%252Fwww.google.com.hk%252F%7C1537952952; _umdata=ED82BDCEC1AA6EB9B9569D3307A0B6774CD04CD48E6631C335859EB6F121D17A7EF569F77AE55242CD43AD3E795C914C51F5D78D238ED76D858A98C95E3A61A8; QCCSESSID=3k4805qvhmb5h9e1bhs7k673e3; hasShow=1; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201537953375089%2C%22updated%22%3A%201537954868524%2C%22info%22%3A%201537359638451%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%224b4ff67d97d1e4b4b710902a66a8bdf6%22%7D; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1537954869',
            'referer': 'https://www.qichacha.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

        # data = {
        #     'key': name
        # }

        response = requests.get(url=webURL, headers=headers, proxies=proxies, timeout=3)

        # print response.content
        pattern = re.compile(r'<a href="(.+?)" class="a-decoration">')
        href = re.search(pattern, response.content).group(1)

        return 'https://www.qichacha.com'+href

    except:
        return 'None'

def getInfo(url,proxies=None):

    try:
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'UM_distinctid=165f1c66f91405-090576f8c1764-1130685c-1aeaa0-165f1c66f92680; zg_did=%7B%22did%22%3A%20%22165f1c66fab1aa-0c33c8fd0a5598-1130685c-1aeaa0-165f1c66fac7be%22%7D; Hm_lvt_3456bee468c83cc63fb5147f119f1075=1537359639,1537416930; _uab_collina=153741693062669146646239; acw_tc=9dff284115374169353944389e736c286ff8760092823790059c8da7d4; PHPSESSID=3008u9r2drm3q5ofn9kh68gmt0; QCCSESSID=3k4805qvhmb5h9e1bhs7k673e3; CNZZDATA1254842228=539091877-1537413217-https%253A%252F%252Fwww.google.com.hk%252F%7C1537952952; _umdata=ED82BDCEC1AA6EB9B9569D3307A0B6774CD04CD48E6631C335859EB6F121D17A7EF569F77AE55242CD43AD3E795C914C51F5D78D238ED76D858A98C95E3A61A8; QCCSESSID=3k4805qvhmb5h9e1bhs7k673e3; hasShow=1; Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1537953777; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201537953375089%2C%22updated%22%3A%201537953777412%2C%22info%22%3A%201537359638451%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%224b4ff67d97d1e4b4b710902a66a8bdf6%22%7D',
            'referer': 'https://www.qichacha.com/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        }

        response = requests.get(url=url, headers=headers, proxies= proxies, timeout=3)
        # print response.content

        pattern = re.compile(r'<span class="cdes">电话：</span><span class="cvlu"> <span style="color: #000;">(.+?)</span>')
        phoneNum = re.search(pattern, response.content).group(1)

        return phoneNum

    except:
        return 'None'

def save_to_csv(line):
    with open('result.csv', 'a') as result:
        writer = csv.writer(result)
        writer.writerow(line)

def main():

    info_list = []
    with open('info.csv', 'rb') as info:
        reader = csv.reader(info)

        for line in reader:
            # print line
            info_list.append(line)

    leave_list = []
    with open('result.csv', 'rb') as old_result:
        reader = csv.reader(old_result)

        for line in reader:
            for i in info_list:
                if line[1] == i[1]:
                    info_list.remove(i)


    # csv_header = ['编号', '企业名称', '申报类别', '拟资助金额', '电话']
    # writer.writerow(csv_header)

    ip_util = IPUtil()
    proxy_ip = ip_util.get_random_ip()
    for i in info_list:
        company = i[1]
        # print company
        companyURL = getURL(company, proxy_ip)
        phone = getInfo(companyURL, proxy_ip)
        # time.sleep(1)
        while phone == 'None':
            proxy_ip = ip_util.get_random_ip()
            companyURL = getURL(company, proxy_ip)
            print 'companyURL:'+ companyURL
            phone = getInfo(companyURL, proxy_ip)
            print 'phone:'+phone
            # time.sleep(1)

        # print proxy_ip
        print phone
        if phone != 'None':
            i.append(phone)
            save_to_csv(i)
            # time.sleep(1)





if __name__ == '__main__':
    # info_list = []
    # with open('info2.csv', 'rb') as info:
    #     reader = csv.reader(info)
    #
    #     for line in reader:
    #         # print line
    #         info_list.append(line)
    #
    # for _ in info_list:
    #     companyURL = getURL(_[1])
    #     print companyURL
    # name = '深圳市利兴隆超声清洗设备有限公司'
    # companyURL = getURL(name)
    # print companyURL
    # getInfo(companyURL)
    main()

    # ip_util = IPUtil()
    # proxy_ip = ip_util.get_random_ip()
    # print proxy_ip
    # name = '深圳市利兴隆超声清洗设备有限公司'
    # companyURL = getURL(name)
    # print companyURL
    # print getInfo(companyURL, {'http': 'http://115.46.66.216:8123'})
    ip = {
        'https': 'https://183.17.231.78:33110'
    }