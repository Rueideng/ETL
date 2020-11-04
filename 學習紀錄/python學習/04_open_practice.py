path = "test.txt"
f = open(path , "r" , encoding="utf-8")
"""
tmp_str=f.read() #全部印出
print(tmp_str)

tmp_str = f.readline() #只讀取一行
print(tmp_str)

tmp_str = f.readline()#只讀取一行
print(tmp_str)



tmp_str=f.readline()
c=0
while tmp_str :
    print("第%s次迴圈:" %(c),tmp_str)
    tmp_str = f.readline()
    c+=1

"""

tmp_str=f.readlines() #
print(tmp_str)
for row in tmp_str: #印出list
    print(row)

f.close()
