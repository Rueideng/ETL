from urllib import  request
from bs4 import BeautifulSoup
"""
#課本寫法
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
headers = {"User-Agent" : useragent}

#Mac 要加下列那行
import ssl
ssl.create_default_https_context = ssl.create_unverified_countext
"""

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url = "https://www.ptt.cc/bbs/Baseball/index.html"

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

#print(res.read().decode("utf-8"))

soup = BeautifulSoup(res.read(), "html.parser")

#print(soup.select("a"))
title = soup.select("div.title")
print(title[0])
print("----------------------------")
print(title[0].select ("a"))
print(title[0].select ("a")[0])
print(title[0].select ("a")[0].text)
print("https://www.ptt.cc" + title[0].select ("a")[0]["href"])



print(title[0].a)
print(title[0].a.text)
