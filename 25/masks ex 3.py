from fnmatch import fnmatch

mask = "1*4022?9"

for number in range(19870 * 2, 10**10, 1987):
    if fnmatch(str(number), mask):
        print(number)
