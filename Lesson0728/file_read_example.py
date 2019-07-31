# 二つめの引数が「r」の場合、read（ファイルを読み込む）
test_file = open("test.txt", "r")
# # 二つめの引数が「w」の場合、write(ファイル上書き)
# open("test.txt", "w")
# # 二つめの引数が「a」の場合、append（ファイルの最後に追加）
# open("test.txt", "a")

# ファイルが読み込めるかのフラグを返却する
# print(test_file.readable())
# ファイルを丸ごとに読み込む
# print(test_file.read())

# 一行ずつ読み込む
# print(test_file.readline())
#
# print(test_file.readline())
#
# print(test_file.readline())

lines = test_file.readlines()
print(lines)

for name in lines:
    print(name.replace("\n", "/"), end="")

test_file.close()

