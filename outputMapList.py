# -*- coding: utf-8 -*-
num = 999

list = ['10020無', '31240TO']

map = {}
outputlist = []

for key in list:
    if(key in map):
        outputlist.append(map[key])
    else:
        num += 1
        setvalue = "★" + str(num)
        map[key] = setvalue
        outputlist.append(setvalue)

f = open('delivery.txt', 'w')

for output in outputlist:
    f.write(output)
    f.write('\n')
f.close()
