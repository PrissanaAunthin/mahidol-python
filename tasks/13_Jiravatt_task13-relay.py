numlist = []
cnt = 0
pos = 0
a = int(input('Enter a number: '))
while (a > 0):
    cnt += 1
    if (cnt == 1) :
        numlist.append(a)
    else :
        pos = 0
        for num in numlist:
            if (a <= num):
                numlist.insert(pos, a)
                break
            pos += 1
        if (pos >= len(numlist)):
            numlist.append(a)
    a = int(input('Enter a number: '))
print(numlist)
