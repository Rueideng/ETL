from selenium.webdriver import Chrome
import time



def get_comment(url):

    driver = Chrome('.\chromedriver')
    url = url
    driver.get(url)
    time.sleep(8)
    js="var action=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(8)

    b=driver.find_element_by_id('disqus-block_1-0')
    te=b.find_element_by_tag_name('iframe')
    url_fra=te.get_attribute("src")
    driver.get(url_fra)
    time.sleep(6)
    contenct=driver.find_elements_by_css_selector('div[class="publisher-anchor-color"] div p')
    contenct_final=[]
    ttry=[]
    for i in contenct:
        ttry=[i.text]
        contenct_final.append(ttry)

    return  contenct_final
    driver.close()












