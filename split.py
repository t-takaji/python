# -*- coding: utf-8 -*-

'''
処理概要
whileで入力ファイルを順に読み込み、1行ずつ出力ファイルに書き出す。
指定した行まで到達すると出力ファイルを閉じ、採番して次の出力ファイルに書き込む
〜以降繰り返し〜
'''

# ファイル名は任意だが、出力ファイルに関しては、%dを含むこと
# ※採番して出力するため
input_file_name = "hoge.csv"
output_file_name_template = "split_%d.csv"

# １ファイルあたりの行数
max_lines = 1000

# 初期処理
line_no = 1
numbering = 1
output_file = open(output_file_name_template % numbering, "w")
input_file = open(input_file_name)
line = input_file.readline()

while line:
    if line_no > max_lines:
        output_file.close()
        numbering += 1
        line_no = 1
        output_file = open(output_file_name_template % numbering, "w")
    output_file.write(line)
    line_no += 1
    line = input_file.readline()

output_file.close()
input_file.close()
