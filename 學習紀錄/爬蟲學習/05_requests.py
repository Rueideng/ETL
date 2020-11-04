#from urllib import  request
import requests
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

res = requests.get(url, headers=headers)

#html string
print(res.text)

soup = BeautifulSoup(res.text, "html.parser")
print(soup)