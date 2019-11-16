#coding:utf-8
import re
f = open('1.txt','r',encoding='utf-8-sig')
data = f.readlines()
f.close()
f1 = open('2.txt','w',encoding='utf-8-sig')
for line in data:
    result = re.sub('\[\d.*\d\]', '', line)
    f1.write(result)
f1.close()
print('success')