from Chef import Chef

# サブクラス名(親クラス名)　　※親クラスのimportは忘れないでください
class Chinese_Chef(Chef):
    def make_special_dish(self):
        print("The chef makes orange chicken")
    def make_fired_rice(self):
        print("The chef makes fried rice")
