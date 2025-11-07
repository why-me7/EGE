max_number = 0
max_divisors = 0
for number in range(568023, 569231):
    count = 0
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
            if number // divisor == divisor:
                count += 1
            else:
                count += 2
    if count >= max_divisors:
        max_number = number
        max_divisors = count
print(max_divisors,max_number )
