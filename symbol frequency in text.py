text = "This is just a string"

frequency = dict()
for symbol in text:
    if symbol in frequency:
        frequency[symbol] += 1
    else:
        frequency[symbol] = 1
max_freq = 0
for key, value in frequency.items():
    if value > max_freq:
        max_freq = value
        symbol = key
print(symbol, max_freq)