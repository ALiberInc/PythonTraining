from Question import Question

question_prompt = [
   "リンゴの色はなんでしょうか?\n(a) 赤\n(b) 紫\n(c) オレンジ\n",
   "バナナの色はなんでしょうか?\n(a) 青緑\n(b) 赤紫\n(c)黄色い\n",
   "イチゴの色はなんでしょうか?\n(a) 黄色い\n(b) 赤\n(c) 青\n"
]

question_and_answer = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]

def run_game(question_and_answer):
    count = 0
    for question in question_and_answer:
        answer = input(question.prompt)
        if answer == question.anwser:
            count += 1

    print("あなたは" + str(count) + "/" + str(len(question_and_answer)) + "が正解です")

run_game(question_and_answer)