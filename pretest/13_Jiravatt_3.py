#This program cannot handle a case where "key" cannot be found yet T_T
exit_status = 0
synonym_list = {'blank': 0}
while (exit_status != 1):
    command = input('Enter your word(s): ')
    if (len(command) == 0) :
        #EXIT !!!
        exit_status = 1
    else :
        temp_list = command.split(' ')
        if (len(temp_list) == 2) :
            #Append into synonym_list
            synonym_list[temp_list[0]] = temp_list[1]
            synonym_list[temp_list[1]] = temp_list[0]
        else :
            #Find its synonym
            print('Its synonym is',synonym_list[temp_list[0]])
