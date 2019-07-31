two_numbers = [4, 5]
two_numbers = (4, 5)
print(two_numbers)
print(two_numbers[0])
# tupleは値の変更、追加、挿入できない、イミュータプルだから
two_numbers[0] = 10

tuple_list = [(1, 2), (3, 4), (5, 6)]
tuple_list[0]

tuple1 = ("みかん",  "りんご")
# オブジェクトの固有番号を表示する
print(id(tuple1))
# tupleの変更ではなく、tupleは新しく生成された
tuple1 += ("バナナ",  "パイナップル")
print(id(tuple1))
tuple2 = tuple1
print(tuple1)
print(tuple2)
print(id(tuple2))

print(tuple1 is tuple2)

#tupleはイミュータプルだから、(1, 2)は同じところを
#指している
tuple1 = (1, 2)
tuple2 = (1, 2)
#listはミュータプルだから、list1とlist2の[1, 2]は
#違うところを指している
list1 = [1, 2]
list2 = [1, 2]

#isはオブジェクトのidの比較
#== はオブジェクトの値を比較
print(tuple1 is tuple2)
print(tuple1 is list1)
print(list1 is list2)
print(list1 == list2)

tuple3 = (1, 2)
tuple4 = (2, 3)

print(tuple3 is tuple4)
