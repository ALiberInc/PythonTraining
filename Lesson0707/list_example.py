# リストの操作１
# list = ["中国", "日本", "アメリカ"]
# print(list)
#
# print(list[1])
#
# new_list = ["中国", "日本", "アメリカ", 1, 2, 3, 3.14]
# print(new_list)

# print(new_list[5])
# print(new_list[-2])
# print(new_list[1:4])
# print(new_list[1:])
# print(new_list[-2:])
# # 下記は無効
# print(new_list[-2:-5])

# new_list[-1] = "韓国"
# print(new_list)

# リストの操作２
lucky_numbers = [3, 6, 7, 8, 9, 10]
names = ["鄭", "佐藤", "周", "黄", "高", "呉"]
print(lucky_numbers)
print(names)
print(lucky_numbers + names)
lucky_numbers.extend(names)
print(lucky_numbers)

new_names = ["鄭", "佐藤", "周", "黄", "高", "呉"]
new_names.append("小野")
print(new_names)

index = new_names.index("周")
print(index)

new_new_names = new_names.copy()
print("new_new_namesは：", end="")
print(new_new_names)

new_names.clear()
print("new_namesは：", end="")
print(new_names)

print("new_new_namesは：", end="")
print(new_new_names)

new_names = ["A", "B", "C", "D", "E", "F"]
print(new_names)

new_names.insert(1, "E")
print(new_names)

print(new_names.count("E"))

print(new_names.__len__())

new_names.sort()
print(new_names)

num_list = [2, 1, 3, 5, 6, 4]
num_list.sort()
print(num_list)

character_list = ["あ", "う", "え", "い"]
character_list.reverse()
print(character_list)

character_list.sort()
print(character_list)

character_list.remove("い")
print(character_list)

character_list.pop()
print(character_list)
