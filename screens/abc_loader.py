class ABCQuestion:
    def __init__(self, contents: str, answers: list, correct_answers: str):
        self.contents = contents
        self.answers = [answer.strip() for answer in answers]
        correct_answers = correct_answers.strip().split()
        self.correct_answers = [ord(answer) - ord('a') for answer in correct_answers]
        print("?")


questions = []

with open("sk.txt", encoding="utf-8") as file:
    file_content = file.readlines()

i = 0
while i < len(file_content) - 2:
    content = file_content[i]
    answers = [file_content[i + x][2:] for x in range(1, 6)]
    correct_answers = file_content[i + 6]

    questions.append(ABCQuestion(content, answers, correct_answers))
    i += 7
