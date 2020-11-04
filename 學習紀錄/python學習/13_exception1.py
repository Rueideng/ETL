#會發生錯誤
'''
def createFile(name):
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
createFile("test/test1")




#例外處理
def createFile(name):
    try:
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except:
        name= name.replace("/","")
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
createFile("test/test1")



#攔截特定例外處理
def createFile(name):
    try:
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except FileNotFoundError:
        name= name.replace("/","")
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except OSError:
        name="test123"
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except:
        print("unknown Exception!")
createFile("test/test1")

#取出特定例外中的資訊 e
def createFile(name):
    try:
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except FileNotFoundError as e:
        print(e)
        print(e.args)
        print(e.errno)
        name= name.replace("/","")
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except OSError as e:
        print(e)
        name="test123"
        with open(name,"w",encoding="utf-8") as f:
            f.write("123")
    except:
        print("unknown Exception!")
createFile("test/test1")

'''

