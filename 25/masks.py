from fnmatch import fnmatch

mask = "1?7602*0"

for number in range(489100 * 2, 10**10, 4891):
    if fnmatch(str(number), mask):
        print(number)
