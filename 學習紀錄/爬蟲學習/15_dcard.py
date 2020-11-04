import requests
import json
from urllib import request
import  re
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
url = "https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555"

res = requests.get(url, headers=headers)

#print(res.text)

json_data=json.loads(res.text) #把外面字串拿近來轉成list或 dictionary

# print(json_data[0])
# print(json_data[1])
# print(json_data[2])
#
# for k in json_data[1]:
#      print(k)

    # Get title
for t in json_data: #每個t都是字典
    title_name = t["title"]
    print(title_name)


    article_url = "https://www.dcard.tw/f/game/p/" + str(t["id"]) #不同型別不能相加 所以把id數字轉換型別
    print(article_url)

    #get images url
    image_url_list = [img ["url"] for img in t["mediaMeta"]]
    print(image_url_list)
    for image_url in image_url_list:
        # request.urlretrieve(image_url, "./dcardimg/" + image_url.split("/")[-1])

        try:
            res_img = requests.get(image_url,headers=headers) #訪問圖片網址
            img_content = res_img.content #存下來像文字
            with open("./dcardimg/" + image_url.split("/")[-1], "wb" ) as f:
                f.write(img_content)
        except OSError as e:
            with open("./dcardimg/" +  (re.sub('["\\","/",":","*","?","<",">","|","\r","\n","\t","-"]', '', image_url.split("/")[-1])), "wb") as f:
                f.write(img_content)
