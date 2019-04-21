numlist = []
min_num = 0
exit_status = 0
# input loop
while exit_status == 0:
    try:
        num = int(input('Enter a number: '))
        numlist.append(num)
    except ValueError:
        exit_status = 1
        

numlist.sort()

# print(numlist)

for i in range(0, len(numlist)):
    print(numlist[i])

    