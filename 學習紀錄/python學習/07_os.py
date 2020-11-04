import os

print("current work dir:",(os.getcwd()))#當前目錄
print("List dir",os.listdir("./"))#當前目錄底下全部印出來  "./"是當前目錄底下

os.mkdir("./test1")
os.makedirs("./test2/test3")
os.remove("./test.txt")
os.rmdir("test1")
os.removedirs("./test2/test3")


if not os.path.exists("test1"): #如果這個test1資料夾不存在  回傳 false
    os.mkdir("test1")