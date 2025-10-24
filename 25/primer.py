number = int(input())
sum_of_digits = 0
while number:
    sum_of_digits += number % 10
    number //= 10
print(sum_of_digits)