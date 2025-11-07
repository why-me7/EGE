number = 700000
count = 0
while count < 5:
    number += 1
    M = 0
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            R += divisor
            R += number // divisor
    if R % 10 == 6:
        print(number, R)
        count += 1