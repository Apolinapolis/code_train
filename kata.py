from selene.support.conditions.have import value


def nb_year(start, percent, aug, needed):
    year = 0
    temp = start

    while temp < needed:
        year += 1
        temp += round(temp * (percent / 100) + aug)

    return year

print(nb_year(1500000, 2.5, 10000, 2000000))





