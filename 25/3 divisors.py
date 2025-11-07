for number in range(101000000, 102000001, 2):
    count = 0
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            if divisor % 2 == 0:
                count += 1
            if (number // divisor) % 2  == 0:
                count += 1
        if count >= 4:
            break
    if count == 3:
        print(number)