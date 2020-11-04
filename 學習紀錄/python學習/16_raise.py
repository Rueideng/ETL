class CustomExceptionError(Exception):
    pass
class CustomExceptionError2(Exception):
    def __int__(self, value):
        self.value = value
    def __repr__(self):
        return self.value
def devide(x,y):
    print("x:",x,"y:",y)
    if y==0:
        raise CustomExceptionError("不可除以0")
    elif not (type(x) in [type(1),type(1,1)]) and (type(y) in [type(1),type(1,1)]):
        raise TypeError("x y必須為數字")
    result = x / y
    return result
if __name__=="__main__":
    try:
        print(devide(2,0))
    except CustomExceptionError as e:
        print(e)

    e = CustomExceptionError2('123123')
    print(e)
