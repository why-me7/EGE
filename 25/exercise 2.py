count = 0
number = 500001
while count < 5:
    summ = 0
    delit=1
    while delit**2 <= number:
        if number % delit == 0:
            summ += delit
            if number // delit > delit:
                summ += number // delit
        delit += 1
    if summ % 10 == 6:
        print(number, summ)
        count += 1
    number += 1