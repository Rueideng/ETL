import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import random
import time
import re


file_data = (r'./kindre_dcocktail')
if not os.path.exists(file_data):
      os.mkdir(file_data)

headers={"user-agent": "瀏覽器資訊"}
url_fir = "https://網址.com/cocktail?page={}&summary=1"


# df = pd.DataFrame(columns=['酒名', 'url','酒譜', '介紹', '步驟', '口味', '評論'])


def number():
    xe=random.randint(1, 1000000)
    return xe

page = 65
numbs=0
list_final=[]

for i in range(0,100):
    res_fir = requests.get(url_fir.format(page), headers=headers)
    soup_first = BeautifulSoup(res_fir.text, "lxml")
    data = {"name": "", "url": "", "ingredient": "", "content": "", "step": "", "flavor": "", "comment": ""}
    time.sleep(30)
    soup_1 = soup_first.select('tr[class="even"] th a')
    soup_2 = soup_first.select('tr[class="odd"] th a')
    url_list=[]

    # URL
    for u in soup_1:
        url_1=u["href"]
        url_list.append(url_1)

    for y in soup_2:
        url_2 = y["href"]
        url_list.append(url_2)
    for i in url_list:
        url=i
        html_url = "https://網址.com/"+url
        print(html_url)
        time.sleep(10)
        data["url"] = html_url
        #標題名稱
        res = requests.get(html_url, headers=headers)
        soup_final = BeautifulSoup(res.text, "lxml")
        title=str.strip(soup_final.select('header[class="clearfix"] h1')[0].text)
        data["name"] = title

        time.sleep(15)

        portion=[]
        #成分


        num_test =  soup_final.select('td[class="qty"]')
        num=0
        temporarily ={}

        for a in num_test:
            material = soup_final.select('td[class="ingredient"]')[num].text

            portion_1 = soup_final.select('td[class="qty"]')[num].text
            portion_2 =  soup_final.select('td[class="units"]')[num].text
            portion= portion_1+portion_2
            # print(portion)
            temporarily[material]=portion
            num+=1
        data["ingredient"]=temporarily

        time.sleep(10)

        #介紹

        judgment_1 = soup_final.select('h6[class="title"]')[1].text
        judgment_2 = soup_final.select('h6[class="title"]')[2].text
        # print(judgment_1)
        # print(judgment_2)

        content_2=""

        if judgment_1 == "History":
            content_2 = soup_final.select('div[class="cocktail-field"]')[1].text.replace("History", "")
        elif judgment_2 == "History":
            content_2 = soup_final.select('div[class="cocktail-field"]')[2].text.replace("History","")

        if   len(content_2) == 0 :
            content="NULL"
            data["content"]=content
        elif  len(content_2) > 0:
            content=content_2
            data["content"] = content
        # print(content)

        time.sleep(6)

        #步驟
        step = soup_final.select('div[class="cocktail-field"]')[0].text.replace("Instructions", "")
        data["step"]=step
        # print(step)

        #口味

        data["flavor"]="NULL"

        # #評論
        try:
            jud_1 = soup_final.select('h6[class="title"]')[1].text
            jud_2 = soup_final.select('h6[class="title"]')[2].text
            jud_3 = soup_final.select('h6[class="title"]')[3].text
            jud_4 = soup_final.select('h6[class="title"]')[4].text
            jud_5 = soup_final.select('h6[class="title"]')[5].text
            jud_6 = soup_final.select('h6[class="title"]')[6].text
            jud_7 = soup_final.select('h6[class="title"]')[7].text
            jud_8 = soup_final.select('h6[class="title"]')[8].text
        except:
            jud_1 = soup_final.select('h6[class="title"]')[1].text
            jud_2 = soup_final.select('h6[class="title"]')[2].text
            jud_3 = soup_final.select('h6[class="title"]')[3].text
            jud_4 = soup_final.select('h6[class="title"]')[4].text
            jud_5 = soup_final.select('h6[class="title"]')[5].text
            jud_6 = soup_final.select('h6[class="title"]')[6].text
        # print(jud_1)
        # print(jud_2)
        # print(jud_3)
        # print(jud_4)
        # print(jud_5)
        # print(jud_6)
        # print(jud_7)
        # print(jud_8)
        # print("-----------------------")
        detail = {}
        comments = {}
        comment_1 = ""
        comment_2 = ""
        comment_3 = ""
        comment_4 = ""
        powerby = ""
        user=""
        discuss_text=""

        #"Notes"判別
        if jud_1 == "Notes":
            comment_1 = soup_final.select('div[class="cocktail-field"]')[1].text.replace("Notes", "")

        # "History"判別
        if jud_1 == "History":
            comment_2 = soup_final.select('div[class="cocktail-field"]')[1].text.replace("History", "")
        elif jud_2 == "History":
            comment_2 = soup_final.select('div[class="cocktail-field"]')[2].text.replace("History", "")

        # "From other users"判別
        if jud_2 == "From other users":
            comment_3 = soup_final.select('div[class="cocktail-book-comment"]')
        elif jud_3 == "From other users":
            comment_3 = soup_final.select('div[class="cocktail-book-comment"]')
        elif jud_4 == "From other users":
            comment_3 = soup_final.select('div[class="cocktail-book-comment"]')
        elif jud_5 == "From other users":
            comment_3 = soup_final.select('div[class="cocktail-book-comment"]')
        elif jud_6 == "From other users":
            comment_3 = soup_final.select('div[class="cocktail-book-comment"]')

        # #"Posted by"張貼者 判別
        # try:
        # if jud_5 == "Posted by":
        #     comment_4 = soup_final.select('div[class="cocktail-field"]')[5].text.replace("Posted by", "")
        # elif jud_6 == "Posted by":
        #     comment_4 = soup_final.select('div[class="cocktail-field"]')[6].text.replace("Posted by", "")
        # elif jud_7 == "Posted by":
        #     comment_4 = soup_final.select('div[class="cocktail-field"]')[7].text.replace("Posted by", "")
        # elif jud_8 == "Posted by":
        #     comment_4 = soup_final.select('div[class="cocktail-field"]')[8].text.replace("Posted by", "")

        #user名稱(評論者)+評論
        j=0

        c=[]
        time.sleep(5)

        discuss_test1=soup_final.select('a[property="foaf:name"]')


        for d in discuss_test1:
            user = d.text
            # print(user)
            discuss_test2 = soup_final.select('div[property="content:encoded"]')[j].text
            discuss_text = str.strip(discuss_test2)
            # print(discuss_text)
            detail[user] = discuss_text
            comments["details"] = detail
            j+=1
            numbs+=1

        # 其他用戶評論
        for ot in comment_3:
            other=ot.text.replace("From other users", "")
            ueer =number()
            detail[ueer]=other
            comments["details"] = detail
            numbs += 1

        #筆記當作評論
        if len(comment_1) > 0:
            for no in range(0,1):
                uer = number()
                detail[uer] = comment_1
                comments["details"] = detail
                numbs += 1
        #內容當作評論
        if len(comment_2) > 0:
            for no in range(0,1):
                ur = number()
                detail[ur] = comment_2
                comments["details"] = detail
                numbs += 1

        data["comment"] = comments
        if data["comment"] == {}:
            data["comment"] = "NULL"
        print(data)
        print("評論比數",numbs)
        json_str = json.dumps(data)
        with open(r'./kindre.json', 'a') as json_file:
            json_file.write(json_str)


    print("頁數",page)

    page+=1





