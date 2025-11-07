with open('Задание 24.txt') as file:
    text = file.readline()
max_len = 0
count = 0
for i in range(len(text)):
    if text[i] != 'NO' or text[i] != 'NP' or text[i] != 'ON' or text[i] != 'OP' or text[i] != 'PN' or text[i] != 'PO':
        count += 1
    else:
        max_len = max(max_len, count)
        count = 0
max_len = max(max_len, count)
print(max_len)