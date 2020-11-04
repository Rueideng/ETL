path= "test.txt"
with open (path,"r",encoding ="utf-8") as f:
    print(f.read())


with open (path,"a",encoding ="utf-8") as f:
    f.write("123456789")