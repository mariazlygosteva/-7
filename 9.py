N, K, R = map(int, input().split())

day = 1
length = N

while length < R:
    length *= (1 + K/100)
    day += 1

print(day)