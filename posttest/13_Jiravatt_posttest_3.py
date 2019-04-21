# This time, I try to program in 'Code' view

synnonym_dict = {}

while True:
    user_txt = input("Enter your word(s): ")
    temp_list = user_txt.split()
    if len(temp_list) == 2:
        synnonym_dict[temp_list[0]] = temp_list[1]
        synnonym_dict[temp_list[1]] = temp_list[0]
    elif len(temp_list) == 1:
        print("Synonym of", temp_list[0], "is", synnonym_dict[temp_list[0]])
    else:
        break

    