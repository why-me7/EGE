def is_prime(number):
    if number <= 1 or number % 2 == 0 and number != 2:
        return False
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True
number = 7000000
count = 0

while count < 5:
    number += 1
    M = 0
    divisor_min = 7000000
    divisor_max = 0
    for divisor in range(1, int(number ** 0.5) + 1):
        if number % divisor == 0:
           if is_prime(divisor):
                divisor_min = min(divisor_min, divisor)
                divisor_max = max(divisor_max, divisor)
           if is_prime(number // divisor):
               divisor_min = min(divisor_min, number // divisor)
               divisor_max = max(divisor_max, number // divisor)
    M = divisor_min + divisor_max
    if M % 100 == 13:
        print(number)
        count += 1
