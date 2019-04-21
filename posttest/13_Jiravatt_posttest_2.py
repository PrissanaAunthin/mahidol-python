# This time, I try to program in 'Code' view

from random import choice

user_input = input("Enter your student's name: ")
stu_list = user_input.split(' ')
print(choice(stu_list))