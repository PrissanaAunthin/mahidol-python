stulist = {}
exit_status = 0
while (exit_status != 1):
    command = input("What is your student's name and their score? ")
    temp_list = command.split(' ')
    if (len(temp_list) == 2) :
        stulist[temp_list[0]] = temp_list[1]
    elif (len(temp_list) == 1) :
        print(temp_list[0],stulist[temp_list[0]])
        del stulist[temp_list[0]]
    else :
        break
    print(stulist)
print(len(stulist))
for i in stulist:
    print(i,stulist[i])
