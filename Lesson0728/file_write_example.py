# 二つめの引数が「w」の場合、write(ファイル上書き)
test_write_file = open("test1.txt", "w")

print(test_write_file.writable())

test_write_file.write("aaaabbbccc")

test_write_file.close()

# 二つめの引数が「a」の場合、append（ファイルの最後に追加）
# test_file = open("test.txt", "a")
test_file = open("test2.txt", "a")

test_file.write("\n佐藤　太郎　３０歳")

test_file.close()


