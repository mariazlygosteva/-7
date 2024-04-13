answer = int(input("Введите ответ, который получила Оля: "))

def check_answer(user_answer):
    correct_answer = 2 ** 12
    correct_answer2 = 2 ** 15
    correct_answer3 = 2 ** 7
    if (user_answer == correct_answer or user_answer == correct_answer2
        or user_answer == correct_answer3):
        return "Верно"
    else:
        return "Неверно"

print(check_answer(answer))