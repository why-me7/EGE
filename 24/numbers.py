with open("24_5832.txt") as file:
    numbers = file.readline()
max_len = count = 0
for i in range(len(numbers)):
    if numbers[i - 1] > numbers[i]:
        count += 1
    else:
        max_len = max(max_len, count)
        count = 1
max_len = max(max_len, count)
print(max_len)
