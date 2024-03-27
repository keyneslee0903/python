age = input('input your age: ')
age = int(age)

if age < 13:
    print('elementary school')
elif age >= 13 and age < 18:
    print('journa and senior school')
elif age >= 18 and age < 22:
    print('colleage')
else:
    print('adult')