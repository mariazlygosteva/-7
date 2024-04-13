def guess_number(N):
    count = 0
    while N > 0:
        N //= 2
        count += 1
    return count

N = int(input("Введите число N: "))

print("Наименьшее количество вопросов:", guess_number(N))