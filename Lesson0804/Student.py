class Student:
    # コンストラクタメソッドを定義する、初期化のため
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    # # コンストラクタメソッドの引数の数を変える
    # def __init__(self, name=None, age=None, sex=None, score=None):
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.score = score

    # クラスメソッドを追加する
    def is_good_student(self):
        if self.score >= 80:
            return True
        else:
            return False