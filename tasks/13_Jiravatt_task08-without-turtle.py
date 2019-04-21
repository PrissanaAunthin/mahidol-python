import random
from math import sqrt, pi

numcases = int(input('How many times do you want to run? '))
numpoints = int(input('How many points do you want? '))
sum_all_cases = 0

for i in range(numcases):
    cnt_hit = 0
    cnt_all = 0
    for i in range(numpoints):
        cnt_all = cnt_all + 1
        x = random.uniform(-150.0, 150.0)
        y = random.uniform(-150.0, 150.0)
        if x**2 + y**2 <= 150.0**2:
            cnt_hit = cnt_hit + 1
    # print('Hit:', cnt_hit, 'from', cnt_all, 'Hit/all =', float(cnt_hit / cnt_all))
    sum_all_cases += float(cnt_hit / cnt_all)

sum_all_cases /= numcases
print('average of hit/all is', sum_all_cases)
print('pi/4 =', pi / 4)
print('diff =', round(abs(sum_all_cases - pi / 4) / (pi / 4) * 100.0, 2), '%')
