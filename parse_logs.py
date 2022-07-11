import os

# カレントディレクトリ
current_directory = os.getcwd().replace(os.sep, '/')

# 入出力のパス
input_path = current_directory + "/logs"
output_file = current_directory + "/result.txt"

# Grep検索対象
grep_target = 'Exception'


def init():
    """ 出力ファイルの中身を削除する。 """
    os.chdir(input_path)

    is_file = os.path.isfile(output_file)
    if is_file:
        os.remove(output_file)


def read_files(file_path):
    """ ログファイルを読み込み、特定文字列を抽出する。 """
    with open(file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        # 指定した文字列を含む行を取得
        GREP_TARGET = [line for line in lines if grep_target in line]
        # 指定した文字列を含まない行を取得
        # GREP_TARGET = [line for line in lines if grep_target1 not in line]
        # and/orで条件追加できる
        # GREP_TARGET = [line for line in lines if grep_target1 in line or grep_target2 in line]

    with open(output_file, mode='a', encoding='utf-8') as f:
        f.writelines(GREP_TARGET)


init()

for file in os.listdir():
    file_path = f"{input_path}/{file}"
    read_files(file_path)
