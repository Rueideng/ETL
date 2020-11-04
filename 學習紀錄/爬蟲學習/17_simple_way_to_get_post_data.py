s="""method: search
searchMethod: true
searchTarget: ATM
orgName: 123
orgId: 456
hid_1: 1
tenderName: 321
tenderId: 321
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/05/30
awardAnnounceEndDate: 109/05/30
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: aaa
hid_2: 1
gottenVendorName: bbb
gottenVendorId: ccc
hid_3: 1
submitVendorName: ddd
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

data = {}
for r in s.split("\n"):
    data[r.split(": ")[0]] = r.split(": ")[1]
print(data)