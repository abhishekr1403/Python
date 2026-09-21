# x = input('enter 1 no:')
# y = input('enter 2 no')
#
# try:
#     z = int(x) / int(y)
# except Exception as e:
#     print('Exception occured is ',e)
#     z = None
# print('Result is ',z)
from logging import exception


# ---------------problem 1----------

def calculate(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'


try:
    grade = int(input("Enter the the grade between 0-100: "))
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0-100!")

    letter = calculate(grade)
except ValueError as e:
    print(f'Invalid !! {e}')
else:
    print(f'Your Letter grade is {letter} ')
finally:
    print('!! Thank you..  !! ')
