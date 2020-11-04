import shutil
import os

os.mkdir("./test1")
os.makedirs("./test2/test3")


shutil.move("./test2/test3","./test1")
shutil.move("./test1","./test2/")
shutil.copytree("./test2/test1/","./test")#把test1底下全部複製到test

shutil.rmtree('./test2/test1')