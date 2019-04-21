# This time, I try to program in 'Code' view

mass = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in cm: '))
bmi = mass / ((height/100)**2)
print('Your BMI is', round(bmi,2))