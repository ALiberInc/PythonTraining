# if elif else及びand/or/notの練習
is_male = True
is_tall = True

if is_male and is_tall:
    print("あなたは背が高い男性です")
elif is_male and not(is_tall):
    print("あなたは男性ですが、背が高くないです")
elif not(is_male) and is_tall:
    print("あなたは背が高い女性です")
else:
    print("あなたは女性です。そして背が高くない")

def if_test(num):
    if num >= 90:
        print("あなたの成績はAです")
    elif num >= 70:
        print("あなたの成績はBです")
    elif num >= 60:
        print("あなたの成績はCです")
    else:
        print("あなたの成績はDです")

if_test(float(input("あなたのスコアを入力してください：")))


# int型のオブジェクトもイーミュタプル
x = 100
y = 100
x = 200

if x != y:
    print("xとyの値は異なる")
else:
    print("xとyの値が同じ")

if x is not y:
    print("xとyの値は異なる")
else:
    print("xとyの値が同じ")







