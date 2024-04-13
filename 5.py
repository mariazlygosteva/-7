N = int(input("Введите максимальный объем (в куб. см): "))

edge = 1
volume = edge ** 3

while volume <= N:
    print(volume, end=" ")
    edge += 1
    volume = edge ** 3