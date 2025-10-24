number = int(input())
if number <= 1 or number % 2 == 0 and number != 2:
    print("NO")
else:
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            print("NO")
            break
    else:
        print("YES")
