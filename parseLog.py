# 入出力のパス
input_path = './test.log'
output_path = './result.txt'

# Grep検索対象
grep_target = '2021-01-27 00:00'
# grep_target2 = 'システムエラー'

# ファイル読み込みとGrep
with open(input_path, mode='r', encoding='utf-8') as f:
    lines = f.readlines()
    GREP_TARGET = [line for line in lines if grep_target in line]
    # not in で含まないでGrepできる
    # GREP_TARGET = [line for line in lines if grep_target not in line]
    # and/or で条件文増やすことができる
    # GREP_TARGET = [line for line in lines if grep_target in line or grep_target2 in line]

# ファイル出力
with open(output_path, mode='w', encoding='utf-8') as f:
    f.writelines(GREP_TARGET)
