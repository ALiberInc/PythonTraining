# x = input("一つ目の数字を入力してください：")
# y = input("二つ目の数字を入力してください：")
# mark = input("計算符号を入力してください：")
#
# result = None
# if mark == "+":
#     result = float(x) + float(y)
# elif mark == "-":
#     result = float(x) - float(y)
# elif mark == "*":
#     result = float(x) * float(y)
# elif mark == "/":
#     result = float(x) / float(y)
# else:
#     print("入力した計算符号が正しくありません")
#
# print(result)

input_x = input("一つ目の数字を入力してください：")
input_y = input("二つ目の数字を入力してください：")
input_mark = input("計算符号を入力してください：")


def calculator(x, y, mark):
    result = None
    if mark == "+":
        result = float(x) + float(y)
    elif mark == "-":
        result = float(x) - float(y)
    elif mark == "*":
        result = float(x) * float(y)
    elif mark == "/":
        result = float(x) / float(y)
    else:
        print("入力した計算符号が正しくありません")

    print(result)


calculator(input_x, input_y, input_mark)
