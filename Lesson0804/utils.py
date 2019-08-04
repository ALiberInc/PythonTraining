import random

count = 1
list = [1, 2, 3, 4, 5]
tuple_a = ("a", "b")

def get_random_int(num):
    return random.randint(1, num)

def get_file_extension(file_name):
    return file_name[file_name.index(".") + 1:]
