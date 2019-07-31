#文字列の操作１
print("Tokyo\nMinato-ku")
print("\"Tokyo\" Minato-ku")

this_place = "Tokyo Minato-ku"
print(this_place)
print(this_place + " is our company address")

print(this_place.lower())
print(this_place.upper())
print(this_place.islower())
print(this_place.lower().islower())
print(len(this_place))
print(this_place.__len__())



#文字列の操作２
print(this_place[0])
print(this_place[3])
print(this_place.index("k"))
print(this_place.index("o"))
print(this_place.index("Min"))
print(this_place.index("あ"))
print(this_place.replace("Minato-ku", "Shinagawa-ku"))
