import requests
from bs4 import BeautifulSoup

headers = {"User=Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

url = "https://www.ptt.cc/bbs/movie/index{}.html" #爬蟲網址

page = 8974 #網頁起始 從網頁上方網址查看
for i in range (0,5):

    res = requests.get(url.format(page),headers=headers) #Html字串

    soup = BeautifulSoup(res.text, "html.parser")

    title_list = soup.select('div.title')
    # print(title_list)
    for title_soup in title_list:
      #print(title_soup)
        try:
            title = title_soup.select('a')[0].text
            print(title)
            title_url = "https://www.ptt.cc"+title_soup.select('a')[0]["href"]
            print(title_url)
        except IndexError as e:
            print(e)
            print(title_soup)

    page -= 1