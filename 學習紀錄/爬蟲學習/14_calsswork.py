import requests
from bs4 import BeautifulSoup
import os
import re

if not os.path.exists("PttGossiping"):
    os.mkdir("PttGossiping")
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

url = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"

ss = requests.session()
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
button = soup.select('button[class="btn-big"]')[0]

hidden = soup.select("input")

data={}
data[button["name"]]=button["value"]

for k in hidden:
    data[k["name"]]=k["value"]


    post_url = "https://www.ptt.cc/ask/over18"
    res_target = ss.post(post_url, data=data, headers=headers)

    final_url = "https://www.ptt.cc/bbs/Gossiping/index.html"

for i in range(0, 15):
    final_res = ss.get(final_url, headers=headers)
    get_soup=BeautifulSoup(final_res.text, "html.parser")
    #print(get_soup)

    title_list=get_soup.select('div.title')

    for title_soup in title_list:
        try:
            new_title = title_soup.select('a')[0].text
            title_url = "https://www.ptt.cc" + title_soup.select('a')[0]["href"]

            illegal = ['~','@','_','-','\\', '/', ':', '*', '?', '"', "'", '<', '>', '|']
            for i in illegal:  # 換掉所有非法字元
                new_title = new_title.replace(i, '_')

            res_article = ss.get(title_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, "html.parser")


            article_select= soup_article.select("#main-content")
            article_contect = article_select[0].text.split("※ 發信站")[0]
            print(article_contect) #文章內容


            #計算 推 噓


            article_select_push=soup_article.select('span[class="hl push-tag"]')
            push_up = 0
            for push_list in article_select_push:
                push_up+=1
            print("推=", push_up)

            article_select_boo = soup_article.select('span[class="f1 hl push-tag"]')
            push_down = 0
            for boo_list in article_select_boo:
                if boo_list.text[0] == "噓":
                    push_down+=1
            print("噓=", push_down)

            article_select_author = soup_article.select('span[class="article-meta-value"]')[0]
            print("文章作者=", article_select_author.text)

            article_select_time = soup_article.select('span[class="article-meta-value"]')[3]
            print("文章撰寫時間=",article_select_time.text)


            try:
                with open("./PttGossiping/%s.txt" % (new_title), "w",encoding="utf-8") as f:  # "./PttMovie/%S 是資料夾內檔案名字,  %(title)是文章標題
                    if article_contect != "":
                        f.write(article_contect)
                        print("---split---", file=f)
                        print("推=", push_up, file=f)
                        print("噓=", push_down, file=f)
                        print("文章作者=", article_select_author.text, file=f)
                        print("文章撰寫時間=", article_select_time.text, file=f)
                        f.close()
            except FileNotFoundError as e:
                print(e)
                print(new_title)
                #with open('./ptthomework/%s.txt'% (re.sub('["[","]","}","{","#","$","%","^","&",")","(","+","_","=","-","@","\\","/",":","*","?","<",">","|"]','',new_title)), 'w',encoding='utf-8') as f:    #去除特殊字元# "./PttMovie/%S 是資料夾內檔案名字,  %(title)是文章標題
                with open("./PttGossiping/%s.txt" % (new_title), "w", encoding="utf-8") as f:
                    f.write(article_contect)
                    print("---split---", file=f)
                    print("推=", push_up, file=f)
                    print("噓=", push_down, file=f)
                    print("文章作者=", article_select_author.text, file=f)
                    print("文章撰寫時間=", article_select_time.text, file=f)
                    f.close()
            except OSError as e_t:
                print(e_t)
                print(new_title)

                with open("./PttGossiping/%s.txt" % (new_title), "w", encoding="utf-8") as f:  # "./PttMovie/%S 是資料夾內檔案名字,  %(title)是文章標題 (title.replace("/", "-"))
                    f.write(article_contect)
                    print("---split---", file=f)
                    print("推=", push_up, file=f)
                    print("噓=", push_down, file=f)
                    print("文章作者=", article_select_author.text, file=f)
                    print("文章撰寫時間=", article_select_time.text, file=f)
                    f.close()
        except IndexError as e:
            print(title_soup)
    url_article = get_soup.select('a[class="btn wide"]')[1]
    previous_url = "https://www.ptt.cc" + url_article['href']
    final_url=previous_url


