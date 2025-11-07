for index, number in enumerate(range(245690, 245757)):
    if number % 2:
        for divisor in range(3, int(number ** 0.5) + 1, 2):
            if number % divisor == 0:
                break
        else:
            print(index + 1, number)
