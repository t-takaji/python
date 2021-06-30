# -*- coding: utf-8 -*-
num = 1019210303120100

f = open('insert.txt', 'w')

for i in range(100000):
    f.write("INSERT INTO hoge VALUES (null,'0','" + str(num) + "');\n")
    num += 1
f.close()
