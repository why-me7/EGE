with open('1.txt') as file:
    text = file.readline()
max_len = 0
count = 0
for i in range(len(text)):
    if text[i] == 'L':
        count += 1
    else:
        max_len = max(max_len, count)
        count = 0
max_len = max(max_len, count)
print(max_len)