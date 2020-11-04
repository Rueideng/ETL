import requests
from bs4 import BeautifulSoup

headers = {"User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

title_url = "https://www.ptt.cc/bbs/movie/M.1590058721.A.C94.html" #爬蟲網址

res_article = requests.get(title_url, headers = headers)

soup_article = BeautifulSoup(res_article.text, "html.parser")

# print(soup_article)
articles_content_list = soup_article.select("#main-content")
print(articles_content_list[0].text.split("※ 發信站")[0])
articles_content = articles_content_list[0].text.split("※ 發信站")[0]