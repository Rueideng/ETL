path = "test.txt"

f=open(path,"w", encoding = "utf-8")
f.write("test write file")
f.close()

f=open(path,"a", encoding = "utf-8")
f.write("test1")
f.write("test2")
f.write("test3\n")
f.write("test4\n")
f.write("test5\n")
f.close()