import requests
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
import liqueur_selenium


file = (r'./cocktail')
if not os.path.exists(file):
   os.mkdir(file)

df = pd.DataFrame(columns=['酒名', 'url','酒譜', '介紹', '步驟', '口味', '評論'])

headers = {
   "User-Agent": '瀏覽器資訊'}
url = 'https://www.網址.com/cocktail-flavors-4779387'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

cocktail_list = []
cocktail_final= []
data = {"name": "", "url": "","ingredient":"", "content": "", "step": "", "flavor": "", "comment":[]}
# 口味網址
f_url = soup.select('ul[id="child-indices_1-0"]')[0].select('li')
for flavor_u in f_url:
   # print("口味:",flavor_u.select('a')[0].text)
   data['flavor'] = flavor_u.select('a')[0].text
   flavor_url = flavor_u.a['href']
   # print(flavor_url)
   res = requests.get(flavor_url, headers=headers)
   soup = BeautifulSoup(res.text, "html.parser")
   # time.sleep(5)

   '''寫法2:
           f_url = soup.select('ul[id="child-indices_1-0"] li a')
       # print(f_url)

       for flavor_u in f_url:

           # print("口味:",flavor_u.select('a')[0].text)
           flavor_url = flavor_u['href']
           # print(flavor_url)
   '''

   # 每款雞尾酒網址
   c_url = soup.select('div[data-tracking-container="true"] div a')
   for c in c_url:
       cocktail_url = c['href']
       if cocktail_url == 'https://www.網址.com/slideshows/spicy-eggnog-cocktails/' or \
           cocktail_url == 'https://www.網址.com/articles/ginger-beer/' or \
           cocktail_url == 'https://www.網址.com/slideshows/best-bloody-mary-recipes/' or    \
           cocktail_url == 'https://www.網址.com/slideshows/salt-cocktails/' or \
           cocktail_url == 'https://www.網址.com/articles/stocktails/' or \
           cocktail_url == 'https://www.網址.com/slideshows/bloody-marys-without-tomato-juice/' or   \
           cocktail_url == 'https://www.網址.com/slideshows/spicy-eggnog-cocktails/' or \
           cocktail_url == 'https://www.網址.com/slideshows/spicy-cocktail-recipes/' or \
           cocktail_url == 'https://www.網址.com/slideshows/best-bloody-mary-recipes/' or \
           cocktail_url == 'https://www.網址.com/articles/smoky-cocktails/' :
           pass
       else:
           data['url'] = cocktail_url
           time.sleep(10)
           print(cocktail_url)

           # print('--------------------------------------------')
           res = requests.get(cocktail_url, headers=headers)
           soup = BeautifulSoup(res.text, "html.parser")

           # 每款雞尾酒名稱
           cocktail_name = soup.select('h1[class="heading__title"]')[0].text
           data['name'] = cocktail_name
           # print(data['name'])

           # 雞尾酒內容 (有些網站要修改一下)
           content_total = soup.select('div[id="article__header--project_1-0"] div p')
           # print(content_total)
           content = []
           for c in content_total:
               con = c.text
               content.append(con)
           data['content'] = content
           # print(data['content'])
           # print("--------------------------------------")

           # 步驟(修)
           step_total = soup.select('ol[id="mntl-sc-block_2-0"] div p')
           # print(step_total)
           step = []
           for s in step_total:
               st = s.text
               step.append(st)
           data['step'] = step
           # print(step)


           tem = {}
           # 酒譜
           ingredients_total = soup.select('ul[id="ingredient-list_1-0"] li')
           for gg in ingredients_total:
               if 'Garnish' in gg.text:
                   pass
               else:
                   ingredients = (gg.text.replace("\n", "").split("("))[0].replace(".", " ").replace("*", "").replace(
                       "oz", "ounce").replace("ounces", "ounce").replace("Medium strawberry",
                                                                         "sheetxx Medium strawberry") \
                       .replace("dashes", "dash").replace("leaves Mint", "Mint leaves").replace("Mint leaves",
                                                                                                "sheetxx Mint leaves").replace(
                       "mint leaves", "sheetxx Mint leaves") \
                       .replace("sprigs", "sprig").replace("Rosemary sprig", " sprig Rosemary").replace(
                       "Jalapeño coins ", "sheetxx Jalapeño coins ") \
                       .replace("1 egg white", "1 ounce egg white").replace("1 Egg white", "1 ounce egg white") \
                       .replace("lemon wedge", "Lemon wedge").replace("Lemon wedge", "wedge Lemon") \
                       .replace("lime wedge", "Lime wedge").replace("Lime wedge", "wedge Lime") \
                       .replace("Vodka or gin", "gin or vodka").replace("gin or vodka", "Gin or vodka") \
                       .replace("slices", "slice").replace("Jalapeño pepper slice", "slice Jalapeño pepper").replace(
                       "Whole egg", "sheetxx Whole egg") \
                       .replace("sticks", "stick").replace("Cinnamon stick", "sheetxx Cinnamon stick").replace(
                       "cloves", "Cloves").replace("Cloves", "sheetxx Cloves") \
                       .replace("Jalapeño round", "sheetxx Jalapeño round").replace("Orange wheels",
                                                                                    "wheels Orange").replace(
                       "2 Lemons", "2 sheetxx Lemons") \
                       .replace("Star", "sheetxx Star").replace("cucumber slice", "slice cucumber").replace(
                       "orange slice", "slice orange") \
                       .replace("Luxardo", "sheetxx Luxardo").replace("Watermelon cubes ",
                                                                      "sheetxx Watermelon cubes ").replace(
                       "Mini watermelon", "sheetxx  Mini watermelon") \
                       .replace("Thai chile pepper", "sheetxx Thai chile pepper").replace("Oysters",
                                                                                          "sheetxx Oysters") \
                       .replace("Spiced-butter-brushed", "sheetxx Spiced-butter-brushed").replace(
                       "1 1” pineapple chunk", "11 sheetxx pineapple chunk").replace("pinches", "pinch") \
                       .replace("fresh lemon juice", "Fresh lemon juice").replace("ounce Fresh lemon juice",
                                                                                  "Fresh lemon juice").replace(
                       "Fresh lemon juice", "ounce Fresh lemon juice") \
                       .replace("simple syrup", "ounce Simple syrup").replace("ounce Simple syrup",
                                                                              "Simple syrup").replace("Simple syrup",
                                                                                                      "ounce Simple syrup") \
                       .replace("ounce St-Germain", "St-Germain").replace("St-Germain", "ounce  St-Germain") \
                       .replace("Basil leaves", "sheetxx Basil leaves").replace("Makrut", "sheetxx Makrut").replace(
                       "Granny", "sheetxx Granny").replace("large","Large")
                   # tem["ing"] = ingredients
                   print("比例+成分: ", ingredients)

                   # key
                   if "dark rum, vodka, tequila, mezcal or gin" in ingredients:
                       ingredientoo = "dark rum, vodka, tequila, mezcal or gin"
                       # tem['ingredient'] = ingredientoo

                       print("成分: ", ingredientoo)
                   elif "Peels and juice of 1/2 orange" in ingredients:
                       ingredientoo = "orange"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "1 lemon peel or wheel" in ingredients:
                       ingredientoo = "lemon"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "bourbon, rye whiskey, Irish whiskey or scotch" in ingredients:
                       ingredientoo = "bourbon, rye whiskey, Irish whiskey or scotch"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "1 Jalapeño pepper, halved " in ingredients:
                       ingredientoo = "Jalapeño pepper"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "1 Lime, juiced" in ingredients:
                       ingredientoo = "Lime"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "Shallot" in ingredients:
                       ingredientoo = "Shallot, roughly chopped"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "Lime, cut into wedges" in ingredients:
                       ingredientoo = "Lime, cut into wedges"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   elif "Kirby slice cucumber, peeled" in ingredients:
                       ingredientoo = "Kirby slice cucumber, peeled"
                       print("成分: ", ingredientoo)
                   elif "1 mini watermelon" in ingredients:
                       ingredientoo = "mini watermelon"
                       print("成分: ", ingredientoo)
                   elif "Whole sheetxx Cloves" in ingredients:
                       ingredientoo = "Whole Cloves"
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)
                   else:
                       ingredientoo = ingredients \
                           .split(', ')[0].split(' tsp ')[-1] \
                           .split(' ounce ')[-1].split(' splash ')[-1].split(' ml ')[-1] \
                           .split(' cup ')[-1].split(' drops ')[-1].split(' splash ')[-1].split(' scoop ')[-1] \
                           .split(' dash ')[-1].split(' pinch ')[-1].split(' barspoon ')[-1].split(' sheetxx ')[-1] \
                           .split(' tbsp ')[-1].split(' bottle ')[-1].split(' teaspoon ')[-1].split(' wedge ')[-1] \
                           .split(' Large ')[-1].split(' slice ')[-1].split(' small chunk ')[-1].split(' wheels')[-1] \
                           .split(' stalk')[-1].split(' sprig')[-1].split('handful')[-1].split('leaves ')[-1]
                       # tem['ingredient'] = ingredientoo
                       print("成分: ", ingredientoo)

                   # value
                   if "cup ounce Fresh lemon juice" in ingredients:
                       proportion = ingredients.split(' cup ounce Fresh')[0]
                       proportion_try = proportion + (" cup ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "cup ounce Simple syrup" in ingredients:
                       proportion = ingredients.split(' cup ounce Simple')[0]
                       proportion_try = proportion + (" cup ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "1 mini watermelon" in ingredients:
                       proportion_try = '1'
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Shallot" in ingredients:
                       proportion_try = "NULL"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Lime, cut into wedges" in ingredients:
                       proportion_try = "NULL"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Kirby slice cucumber, peeled" in ingredients:
                       proportion_try = "NULL"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Peels and juice of 1/2 orange" in ingredients:
                       proportion_try = "Peels and juice of 1/2"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Whole sheetxx Cloves" in ingredients:
                       proportion_try = "1 tbsp"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "ounce" in ingredients:
                       proportion = ingredients.split(' ounce ')[0]
                       proportion_try = (proportion.replace(" ", "")) + (" ounce")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "1 lemon peel or wheel" in ingredients:
                       proportion_try = "peel or wheel"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "sheetxx" in ingredients:
                       proportion_try = ingredients.split(' sheetxx')[0]
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif "handful" in ingredients:
                       proportion = ingredients.split(' handful')[0]
                       proportion_try = proportion + (" handful ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif "wheels Jalapeño" in ingredients:
                       proportion = ingredients.split(' wheels Jalapeño')[0]
                       proportion_try = proportion + (" wheels ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "wheels Orange" in ingredients:
                       proportion = ingredients.split(' wheels Orange')[0]
                       proportion_try = proportion + (" wheels ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "wheels " in ingredients:
                       proportion = ingredients.split(' wheels  ')[0]
                       proportion_try = proportion + (" wheels ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif "stalk" in ingredients:
                       proportion = ingredients.split(' stalk ')[0]
                       proportion_try = proportion + (" stalk")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "small chunk" in ingredients:
                       proportion = ingredients.split(' small chunk ')[0]
                       proportion_try = proportion + (" small chunk")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif ", cut into wedges" in ingredients:
                       proportion_try = ingredients.split(', ')[-1]
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "sprig" in ingredients:
                       proportion = ingredients.split(' sprig')[0]
                       proportion_try = proportion + (" sprig ")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "wedge" in ingredients:
                       proportion = ingredients.split(' wedge ')[0]
                       proportion_try = proportion + (" wedge")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "bottle" in ingredients:
                       proportion = ingredients.split(' bottle ')[0]
                       proportion_try = proportion + (" bottle")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "teaspoon" in ingredients:
                       proportion = ingredients.split(' teaspoon ')[0]
                       proportion_try = proportion + (" teaspoon")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "splash" in ingredients:
                       proportion = ingredients.split(' splash ')[0]
                       proportion_try = proportion + (" splash")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "barspoon" in ingredients:
                       proportion = ingredients.split(' barspoon ')[0]
                       proportion_try = proportion + (" barspoon")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "slice" in ingredients:
                       proportion = ingredients.split(' slice ')[0]
                       proportion_try = proportion + (" slice")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "Large" in ingredients:
                       proportion = ingredients.split(' Large ')[0]
                       proportion_try = proportion + (" Large")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif "pinch" in ingredients:
                       proportion = ingredients.split(' pinch ')[0]
                       proportion_try = proportion + (" pinch")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif "ml" in ingredients:
                       proportion = ingredients.split(' ml')[0]
                       proportion_try = proportion + (" ml")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "leaves Sage" in ingredients:
                       proportion = ingredients.split(' leaves Sage')[0]
                       proportion_try = proportion + (" leaves")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "drops" in ingredients:
                       proportion = ingredients.split(' drops')[0]
                       proportion_try = proportion + (" drops")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "dash" in ingredients:
                       proportion = ingredients.split(' dash')[0]
                       proportion_try = proportion + (" dash")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "splash" in ingredients:
                       proportion = ingredients.split(' splash')[0]
                       proportion_try = proportion + (" splash")
                       tem[ingredientoo] = proportion_try
                   elif "tsp" in ingredients:
                       proportion = ingredients.split(' tsp')[0]
                       proportion_try = proportion + (" tsp")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "tbsp" in ingredients:
                       proportion = ingredients.split(' tbsp')[0]
                       proportion_try = proportion + (" tbsp")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "cup" in ingredients:
                       proportion = ingredients.split(' cup')[0]
                       proportion_try = proportion + (" cup")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif "scoop" in ingredients:
                       proportion = ingredients.split(' scoop')[0]
                       proportion_try = proportion + (" scoop")
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   elif ("ounce" and "cold") in ingredients:
                       proportion_a = ingredients.split(' oz')[0] + (" ounce")
                       proportion_b = ingredients.split(',')[-1]
                       proportion_try = proportion_a + proportion_b
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)

                   elif ', ' in ingredients:
                       proportion_try = ingredients.split(', ')[-1]
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   else:
                       proportion_try = "NULL"
                       tem[ingredientoo] = proportion_try
                       print("比例: ", proportion_try)
                   data["ingredient"]=tem

                   print("---------------------------------")

           #評論
           comment=liqueur_selenium.get_comment(cocktail_url)
           if comment==[]:
               data["comment"]="NULL"
           else:
               data["comment"]=comment

           cocktail_list.append(list(data.values()))
           # print(cocktail_list)
   # cocktail_final+= cocktail_list
   # print(cocktail_final)
print(cocktail_list)
print("--------------------------------")

dff = df.append(pd.DataFrame(cocktail_list, columns=['酒名', 'url','酒譜', '介紹', '步驟', '口味', '評論']))
dff.to_csv(r'./cocktail/cocktail_3.csv', index=False, encoding="utf-8-sig")

