count = 0
n = 500000000
while count < 5:
    #print(n)
    n += 1
    m = 1
    divisors = set()
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            divisors.add(divisor)
            divisors.add(n // divisor)
    if len(divisors) > 5:
        divisors = sorted(divisors)
        m = divisors[0] * divisors[1] * divisors[2] * divisors[3] * divisors[4]
        if (m < n):
            count += 1
            print(m)
