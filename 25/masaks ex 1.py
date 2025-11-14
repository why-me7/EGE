from fnmatch import fnmatch

mask = "1?4*6?8"

for number in range(26220 * 2, 10**8, 2622):
    if fnmatch(str(number), mask):
        print(number, number // 2622)
