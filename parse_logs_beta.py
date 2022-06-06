# -*- coding: utf-8 -*-

'''
操作ログを抽出します。
検索対象に会員SEQや特定の行動を設定することでそのセッションIDから操作ログを抽出します。
'''
import os

## 設定情報
######################################################################
# ファイルパス
input_directory_path = "C:/test"
output_path = "C:/result.txt"
# 検索対象
grep_target1 = "EXCEPTION"
######################################################################

os.chdir(input_directory_path)


def read_text_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # 指定した文字列を含む行を取得
        GREP_TARGET = [line for line in lines if grep_target1 in line]
        # orで条件追加できる
        # GREP_TARGET = [line for line in lines if grep_target1 in line or grep_target2 in line]
        SESSION_ID_LIST = [item.split()[3] for item in GREP_TARGET]

    # 重複行削除
    result = list(set(SESSION_ID_LIST))
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # 指定した文字列を含む行を取得
        ACTION = [line for line in lines for a in result if a in line]

    with open(output_path, mode='w', encoding='utf-8') as f:
        f.writelines(ACTION)


for file in os.listdir():
    file_path = f"{input_directory_path}\{file}"
    read_text_file(file_path)
