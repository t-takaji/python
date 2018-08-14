#_*_ coding:utf-8 _*_

import calendar


def check_leap_year(year):
    # 閏年判定
    if calendar.isleap(year):
        print(str(year) + "年は閏年です。")
    else:
        print(str(year) + "年は平年です。")


def main():
    input_year = input("年を入力してください(yyyy)：")
    check_leap_year(input_year)


if __name__ == "__main__":
    main()
