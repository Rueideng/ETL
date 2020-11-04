import time

print("123","321")
print("123","321",sep="|")
print("123","321",sep="|",end="")
print("123","321",sep="|",end="")
print("file123123",file=open("test.txt","w"))

f=open("test.txt", "a")
for i in range(0,5):
    #time.sleep(5)
    print("123654789", file=f)