try:
    # value = 10 / 0
    # number = int(input("一つの数字を入力してください: "))
    # print(number)

    list = [1,2,3]
    print(list[3])
except ZeroDivisionError:
    print("0で割ることができません")
except ValueError:
    print("入力したものは数字ではありません。数字を入力してください。")
except:
    print("予想外のエラーが発生しました")
