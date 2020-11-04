from selenium.webdriver import Chrome
import requests
from bs4 import  BeautifulSoup
driver = Chrome("./chromedriver")

url = "https://www.ptt.cc/bbs/index.html"

driver.get(url)

driver.find_element_by_class_name("board-name").click() #自動開啟網頁進去八卦版
driver.find_element_by_class_name("btn-big").click()    #自動按取滿18歲


cookie = driver.get_cookies()
for c in cookie:
 print(c)