import requests
import  json
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
url = "https://buzzorange.com/techorange/wp-admin/admin-ajax.php"

#data是訪問伺服器必須要帶入的資料 因此要寫並帶入
data={"action": "fm_ajax_load_more",
      "nonce": "d8c08f1381",
      "page": "1"}# page頁數 如果要多頁可以寫迴圈

res = requests.post(url, headers=headers, data=data) #用POST方式取得request
json_data = json.loads(res.text)#利用json 轉換型別(把外面字串拿近來轉成list或 dictionary)

# print(json_data)
# print(json_data.keys())
# print(json_data["data"]) #html string

soup = BeautifulSoup(json_data["data"],"html.parser") #轉成beautifulsoup格式 可以抓取想要資料
title_list = soup.select('a[class="post-thumbnail nljf"]')
#print(title_list)
for t in title_list:
    print(t)
    print(t["onclick"])
