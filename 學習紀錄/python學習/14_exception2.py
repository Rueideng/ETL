'''#執行錯誤
def add(x,y):
    output = x+y
    return output

print(add(3,"s"))



#例外處理
def add(x,y):
    try:
        output = x+y
    except TypeError as e:
        output=int(x)+int(y)
    return output
print(add(3,"5"))


#例外處理無法處理 回傳None
def add(x,y):
    try:
        output = x+y
    except TypeError as e:
        print(e)
        try:
            output = int(x) + int(y)
        except ValueError as e:
            return None
    return output
print(add(3,"5"))
print(add(3,"x"))


#例外處理else finally
def add(x,y):
    try:
        output= x+y
    except TypeError as e:
        print(e)
        try:
            output = int(x) + int(y)
        except ValueError as e:
            return None
    else :
        print("Answer is",output)
    finally:
        print("無論如何都會執行")
    return output
print(add(3,"5"))
print(add(3,"x"))
print(add(3,5))
'''

