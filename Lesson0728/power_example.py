# print(3**3)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num

    return result

res = raise_to_power(10, 3)
res = res + 100

print(res)
