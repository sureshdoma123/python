import csv
import matplotlib.pyplot as plt

event=[]
coll=[]
with open("real_data.csv")as f1:
    data=list(csv.reader(f1))
    for i in data[1:]:
        event.append(i[6])
        if i[6] not in event:
            event.append(i[6])
    for i in data[1:]:
        if i not in coll and (i[6]=="Evening"):
            coll.append(i[2])

dic={}
l=[]
for i in coll:
    if i not in l:
        l.append(i)
for i in l:
    dic[i]=coll.count(i)
print(dic)

plt.bar(dic.keys(),dic.values())
plt.show()
