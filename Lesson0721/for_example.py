# forループの書き方①
list1 = [10, 12, 8, "aaa"]

for value in list1:
    print(value)

print("--------------")

tuple1 = (1, 2, "aaaa", 4)

for value in tuple1:
    print(value, end=" ")

print()
print("--------------")

season = {
    "spring": "春",
    "summer": "夏",
    "autumn": "秋",
    "winter": "冬"
}

for key in season:
    print(key)
    print(season.get(key))

# forループの書き方②
for letter in "abcd edf":
    print(letter)

# forループの書き方③
for index in range(10):
    print(index)

print("--------------")

for index in range(3, 10):
    print(index)

print("--------------")

list1 = [10, 12, 8, "aaa"]

for index in range(len(list1)):
    print(list1[index])