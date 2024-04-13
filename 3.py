import math

while True:
    num = int(input("Введите число: "))

    if math.isqrt(num) ** 2 == num:
        print("Это число является полным квадратом.")
        break
    else:
        print("Это число не является полным квадратом. Введите другое число.")