import json


# file = open("./New5.json", 'r',encoding='utf-8')
# papers = []
# for i in file.readlines():
#     dic = json.loads(i)
#     papers.append(dic)
# print(papers)

with open("./New5.json",'r',encoding='utf-8') as g:
	result_data = json.load(g)
q=1
for i in result_data:
    print(i)
    q+=1
    print(q)