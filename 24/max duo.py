with open('107_24.txt') as file:
    text = file.readline()
text = text.replace('AB', 'x')
text = text.replace('CB', 'x')
max_len = 0
count = 0
for i in range(len(text)):
    if text[i] == 'x':
        count += 1
    else:
        max_len = max(max_len, count)
        count = 0
max_len = max(max_len, count)
print(max_len)