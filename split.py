# -*- coding: utf-8 -*-

'''
処理概要
whileで入力ファイルを順に読み込み、1行ずつ出力ファイルに書き出す。
指定した行まで到達すると出力ファイルを閉じ、採番して次の出力ファイルに書き込む
〜以降繰り返し〜
'''

# ファイル名は任意だが、出力ファイルに関しては、%dを含むこと
# ※採番して出力するため

# import glob
# input_file_list = glob.glob("./input/*.csv") globを使えば、ファイルリストの取得が可能
# input_file_name = input_file_list[0]

input_file_name = "t_GoodsVisitor20190307_171507.csv"
output_file_name = "split_%d.csv"

# １ファイルあたりの行数
max_lines = 10000
# 対話型例　下記の場合、int(max_lines)のようにint型で判別すると良い
# max_lines = input("1ファイルあたりの最大行数を入力してください。>>> ")

# 初期処理
line_no = 1
numbering = 1
output_file = open(output_file_name % numbering, "w")
# output_file = open("./output/"+output_file_name % numbering, "w")　フォルダ指定も可　フォルダが存在しない場合エラー
input_file = open(input_file_name)
line = input_file.readline()

while line:
    if line_no > max_lines:
        output_file.close()
        numbering += 1
        line_no = 1
        output_file = open(output_file_name % numbering, "w")
    output_file.write(line)
    line_no += 1
    line = input_file.readline()

output_file.close()
input_file.close()
