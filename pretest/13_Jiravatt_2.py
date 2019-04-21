import random


stu_list = input('Enter your student list: ').split(' ')
print('A lucky student is',random.choice(stu_list))
