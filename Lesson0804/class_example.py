# from pythonファイル名 import クラス名
from Student import Student

student1 = Student("LiLei", 20, True, 85.5)
student2 = Student("HanMeimei", 19, False, 75.0)

# デフォルト値Noneを使用するコンストラクタを呼び出す（複数コンストラクタメソッドを実現できる）
# student1 = Student("LiLei", 20, True)
# student2 = Student("HanMeimei", 19, False)

# print(student1.name)
# print(student2.name)
#
# print(student1.age)
# print(student2.age)
#
# print(student1.sex)
# print(student2.sex)
#
# print(student1.score)
# print(student2.score)

print(student1.is_good_student())
print(student2.is_good_student())