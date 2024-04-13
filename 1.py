quantity = 0
for number in range (100, 999):
    if number % 17 == 0:
       print(f'{number} ' '')
       quantity += 1
print(f'{quantity}')