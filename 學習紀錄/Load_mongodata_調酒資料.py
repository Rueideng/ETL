import nltk
import string
from gensim.models import word2vec
import re
import time
import csv
from pymongo import MongoClient
from math import isnan

uri = f'mongodb://使用者名稱:名稱@IP:27017/'

client = MongoClient(uri)       # 連線本地MongoDB資料庫
# ---------------------------------------------------    從mongo中取資料  ---------------------------------------------------
db = client.cocktail  # DB名
collections = db.all_cocktail  # 桶子名



def get_tokens(text): #把字詞變小寫去除不必要的標點符號與文字
    lowers = re.sub(r'\n|(NULL)|®|\d|[^\w]|[ΆΈ-ώ]|[^a-zA-Z]', ' ', text).lower() # 全部變小寫並清洗
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation) #string.punctuation
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)#分詞

    return tokens



#=======================================================================
def safetoken(word): #儲存所有的待訓練字句
    segSaveFile = 'liquer_test.txt'
    with open(segSaveFile, 'ab+') as saveFile:
        words=word.encode('utf-8')
        saveFile.write(words)
        saveFile.write('\n'.encode())




def isnan(num):
    return num != num





def loadMongofile_add():
    word=""
    list_w=""

    for item in collections.find():
        cocktail_name = item['name']
        print("酒名:",cocktail_name)
        cocktail_comment_all = item['comment']
        print("所有使用者評論:",cocktail_comment_all)
        print(type(cocktail_comment_all))
        try:
            if isnan(float(cocktail_comment_all)) == True:
                continue
        except:
            if cocktail_comment_all == 'null' or  cocktail_comment_all == "" or cocktail_comment_all == " nan" or cocktail_comment_all == "None":
                continue
            else:
                # print( cocktail_comment_all == "")
                cocktail_all = cocktail_comment_all.replace("user","").replace("name","").replace("text","")
                tokens=get_tokens(cocktail_all)
                # print(tokens)

                tks = ""
                for tk in tokens:
                    tks = tks + " " + tk
                word=word +"\n"+tks
                print(word)
        # safetoken(word)
        # print(word)
if __name__ == "__main__":
    loadMongofile_add()