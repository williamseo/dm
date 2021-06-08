#!/d/sysutils/conda/python.exe
# -*- coding: utf-8 -*-

f = open('address.txt','r',encoding='utf-8')
while True:
    line = f.readline()
    if not line: break
    elementsL = line.split('|')
    print('%s %s %s'% (elementsL[1],elementsL[2],elementsL[3]),'%s-%s'%(elementsL[6],elementsL[7]))
