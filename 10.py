count = 0
prev_temp = float(input())

while True:
    temp = float(input())
    if temp == 0:
        break
    if temp < prev_temp:
        count += 1
    prev_temp = temp

print(count)