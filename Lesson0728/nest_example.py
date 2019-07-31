number_grid = [
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9],  # 2
    [0]         # 3
]

# print(number_grid[0])
for value1 in number_grid[0]:
    print(value1, end="/")

for value2 in number_grid[1]:
    print(value2, end="/")
# print(number_grid[1])
print(number_grid[2][2])
# print(number_grid[1][1])

for row in number_grid:
    for column in row:
        print(column)
