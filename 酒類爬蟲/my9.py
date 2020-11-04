import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import random
import time
import re

file_data = (r'./my9')
if not os.path.exists(file_data):
      os.mkdir(file_data)
headers={"user-agent": "瀏覽器資訊"}
url_fir = "https://www.網址.com.tw/collections/%E5%A8%81%E5%A3%AB%E5%BF%8C?page={}"

df = pd.DataFrame(columns=['酒名','酒廠','URL','年份','產地','酒精度(%)','照片','內容','評論','價錢'])


page = 1

list_final=[]

for i in range(0,37):
    res_fir = requests.get(url_fir.format(page),headers=headers)
    soup_first = BeautifulSoup(res_fir.text, "lxml")

    # list_one = {"en_name": "", "cn_name": "", "winery": "", "url": "", "year":"", "area": "", "alcohol": "", "photo": "", "content": "", "comment":"", "money":""}
    list_one = {"cn_name": "", "winery": "", "url": "", "year":"", "area": "", "alcohol": "", "photo": "", "content": "", "comment":"", "money":""}

    my_list = []
    list_try = []
    print("-------------page=", page)
    page_product = soup_first.select("a.product-info__caption ")
    t=0
    for o in page_product:
        html_a=o["href"]
        # html_a = soup_first.select("a.product-info__caption ")[t]["href"]
        # print("html_a=",html_a)
        html_url="https://www.網址.com.tw"+html_a
        print(html_url)
        res = requests.get(html_url,headers=headers)
        # time.sleep(random.uniform(1, 3))
        # time.sleep(2)
        soup = BeautifulSoup(res.text, "lxml")


         #URL
        list_one["url"]=html_url

        #照片擷取
        photo = soup.find('div',{'class':'gallery-cell'})
        photo_url = "https://"+ photo['data-image-height'].split('//')[1].split('?')[0]
        list_one["photo"]=photo_url

        # #英文名字
        # en_name = soup.select("p[itemprop='name']")[0].text
        # list_one["en_name"]=en_name

        #中文名字
        cn_name = soup.select("h1.product_name")[0].text
        list_one["cn_name"] = cn_name

        #價錢
        money = soup.select("span.was_price")[0].text
        print("money=",money)
        if len(money) > 0 :
            list_one["money"] = money
        elif money=="":
            cell_money = soup.select("span.current_price")[0].text
            if len(cell_money) > 0 :
                print("cell_money=",cell_money)
                list_one["money"] = cell_money
            else:
                sale_money = soup.select("span.current_pricehidden")[0].text
                print("sale_money=",sale_money)
                list_one["money"] =sale_money

        print("list_one['money']",list_one["money"])

        #內容
        content = soup.select("div[class='product-collapse white-block'] p ")


        q=[]
        for j in content:
            if j.text =='':
                continue
            q.append(j.text)
            h='，'.join(q)
        try:
            s= h.split('數量有限，贈完為止！(贈品示意圖如下)')[1]
            list_one["content"]=s
        except:
            list_one["content"]=h

        if content ==  []:
            list_one["content"] ="NULL"

        #print(content)

        # 品牌/酒莊&產區 判別
        try:
            n = soup.select("div.product-details-item ")[3].span.text
            temporary = soup.select("div.product-details-item ")[3].a.text
            if n == "品牌/酒莊":
                list_one["winery"] = temporary
            elif n == "產區":
                list_one["area"] = temporary
        except:
            if n == "容量":
                list_one["area"] = "NULL"

        # 酒精度&品牌/酒莊 判別
        try:
            m = soup.select("div.product-details-item ")[4].span.text
            temporary_a = soup.select("div.product-details-item ")[4].div.text.replace("%","")
            if m == "酒精度":
                list_one["alcohol"] = temporary_a
            elif m == "品牌/酒莊":
                list_one["winery"] = temporary_a
        except:
            continue

        # 酒精度判別
        try:
            s = soup.select("div.product-details-item ")[5].span.text
            temporary_b = soup.select("div.product-details-item ")[5].div.text.replace("%","")
            if s == "酒精度":
                list_one["alcohol"] = temporary_b
        except:
            continue

        #都沒有年份 所以設NULL
        list_one["year"]="NULL"

        # 都沒有評論 所以設NULL
        list_one["comment"] = "NULL"

        #如果沒有酒精度就設為空
        if list_one["alcohol"]=="":
            list_one["alcohol"]="NULL"

        # 如果沒有產區就設為空
        if list_one["area"]=="":
            list_one["area"]="NULL"

        list_try = list(list_one.values())
        my_list.append(list_try)


        t=t+1

    # print(my_list)
    list_final+=(my_list)

    page+=1

# print(list_final)

dff=df.append(pd.DataFrame(list_final,columns=['酒名','酒廠','URL','年份','產地','酒精度(%)','照片','內容','評論','價錢']))
dff.to_csv(r'./my9/my9.csv',index=False,encoding="utf-8-sig")
