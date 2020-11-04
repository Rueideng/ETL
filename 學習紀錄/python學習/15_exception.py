#Excrption類別接住所有例外處理
import  sys
'''

try:
    print(1+"2")
except Exception as e:
    print(e)


try:
    sys.exit("123")
except SystemExit as e :
    print("接住例外")
    print(e)
    
try:
    sys.exit("123")
except SystemExit as e:
    print("接住例外")
    print(e)

'''

