#pythonの関数定義はdefキーワードを使用する
#インデントがあるソースブロックは関数の中身
def say_hi(name, age):
    print("こんにちは、" + name
          + "さん、あなたは" + str(age) + "歳")

#実行順番は、関数が呼び出されるまで実行しない
print("これから関数を実行します")
say_hi("山田", 22)
print("ここまで関数の実行が終了しました")


# 関数のリターン及びリターン後の処理実行
# Noneはほかの言語だったら、null
def cube(num):
    return num * num * num
    print("ここに来るのかな")


print(cube(2))




