from urllib import  request
from bs4 import BeautifulSoup
"""
#課本寫法
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
headers = {"User-Agent" : useragent}
"""

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url = "https://www.ptt.cc/bbs/Baseball/index.html"

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

#print(res.read().decode("utf-8"))

soup = BeautifulSoup(res.read(), "html.parser")
#print(soup)

#logo = soup.findAll("a", {"id": "logo"})
#logo = soup.findAll("a", id= "logo")
#logo = soup.select('a[id="logo"]')
logo =soup.select("a#logo") #課本沒有的 選擇器 寫法


print(logo)
print(logo[0])
print(logo[0].text) #text把標籤以外的內容取出來
print("https://www.ptt.cc" + logo[0]["href"])