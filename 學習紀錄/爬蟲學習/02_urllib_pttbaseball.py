from urllib import  request
"""
#課本寫法
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
headers = {"User-Agent" : useragent}
"""

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
url = "https://www.ptt.cc/bbs/Baseball/index.html"

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

print(res.read().decode("utf-8"))