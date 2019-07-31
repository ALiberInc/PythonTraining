month_conversions = {
    "Jan": "一月",
    "Feb": "二月",
    "Mar": "三月",
    "Apr": "四月",
    "May": "五月",
    "Jun": "六月",
    "Jul": "七月",
    "Aug": "八月",
    "Sep": "九月",
    "Oct": "十月",
    "Nov": "十一月",
    "Dec": "十二月",
    13: "1000000",
    14: ["1", "2"]
}

# value = month_conversions["Jan"]
value = month_conversions.get("Jan")
print(value)

value2 = month_conversions.get("Luv", "値が存在しない")
print(value2)

value3 = month_conversions.get(13)
print(value3)

value4 = month_conversions.get(14)
print(value4[0])
