import sys

#接收外部參數(List) input_test 為自己設定
input_test = sys.argv
#print(input_args)


#因為第0個是檔案名稱所以從第一個開始
input_test= input_test[1:]
output=0
for i in input_test:
    output +=int(i)#取出為字串 使用int轉換
print(output)