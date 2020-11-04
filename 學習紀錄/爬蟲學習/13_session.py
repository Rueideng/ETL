import  requests
from bs4 import BeautifulSoup

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

url="https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"


ss = requests.session()

#session 1
#res = requests.get(url, headers=headers)
res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
button = soup.select('button[class="btn-big"]')[0]
print(button)
print(button["name"])
print(button["value"])
print(ss.cookies)
print("------------------------------------------------------")


hidden = soup.select("input")
print(hidden)

print("------------------------------------------------------")
data= {}
data[button["name"]]= button["value"]
for k in hidden:
    data[k["name"]]= k["value"]

print(data)
print("------------------------------------------------------")
#session 2
target_url = "https://www.ptt.cc/ask/over18"
#res_target = requests.post(target_url, data=data, headers=headers)
res_target = ss.post(target_url, data=data, headers=headers)



#session 3
final_url = "https://www.ptt.cc/bbs/Gossiping/index.html"
#final_res = requests.get(final_url, headers=headers)
final_res = ss.get(final_url, headers=headers)
print(final_res.text)

print("------------------------------------------------------")
#查看 session cookies
print(ss.cookies)

