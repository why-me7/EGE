for number in range(210235, 210301):
    divisors = set() #пустое множество
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            divisors.add(divisor)
            divisors.add(number // divisor)
            if len(divisors) > 4:
                break
    if len(divisors) == 4:
        print(*sorted(divisors))