# -*- coding: utf-8 -*-

'''
操作ログを抽出します。
検索対象に会員SEQや特定の行動を設定することでそのセッションIDから操作ログを抽出します。
'''
import os

# ログ配置ディレクトリ
input_directory_path = os.getcwd().replace(os.sep, '/') + "/log"
# 出力ファイル
output_file = os.getcwd().replace(os.sep, '/') + "/result.txt"
# 検索対象
grep_target = "exception"


def init():
    # ディレクトリ移動
    os.chdir(input_directory_path)

    # 出力ファイル初期化
    is_file = os.path.isfile(output_file)
    if is_file:
        os.remove(output_file)

def read_files(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # 指定した文字列を含む行を取得
        GREP_TARGET = [line for line in lines if grep_target in line]
        # ターゲットのセッションIDをリスト化
        SESSION_ID_LIST = [item.split()[3] for item in GREP_TARGET]

    # 重複行削除
    session_id_list = list(set(SESSION_ID_LIST))

    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # 指定した文字列を含む行を取得
        ACTION = [line for line in lines for s in session_id_list if s in line]

    with open(output_file, mode='a', encoding='utf-8') as f:
        f.writelines(ACTION)

init()

for file in os.listdir():
    file_path = f"{input_directory_path}\{file}"
    read_files(file_path)
