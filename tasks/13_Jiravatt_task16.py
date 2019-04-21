stulist = {}
for __count in range(5):
    command = input("What is your student's name and their score? ")
    temp_list = command.split(' ')
    if (len(temp_list) == 2) :
        stulist[temp_list[0]] = temp_list[1]
    else :
        break
print('You have entered records of',len(stulist),'student')
for i in stulist:
    print(i,stulist[i])
