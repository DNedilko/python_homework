
import re
def valid(numbers):
    return bool (re.match('\d',numbers))

def get_weeks(numbofweeks):
    numberofweeks=input(numbofweeks)
    while not valid(numberofweeks):
        numberofweeks=input(numbofweeks)
    return int(numberofweeks)

def get_mounth(numbofmounth):
    numberofmounth = input(numbofmounth)
    while not valid(numberofmounth):
        numberofmounth = input(numbofmounth)
    return int(numberofmounth)

def get_year(numbofyears):
    numberofyears = input(numbofyears)
    while not valid(numberofyears):
        numberofyears = input(numbofyears)
    return  int(numberofyears)

def program():
    weeks = get_weeks("Введіть кількість тижнів ")
    mounth = get_mounth("Введіть кількість місяців ")
    years = get_year("Введіть кількість років ")
    return (weeks*7)+(mounth*30)+(years*365)

print("Неділько Дарина Вікторівна \n Лабораторна робота №1 \n Варіант 14 \n Завдання №2. Знаходження кількості днів ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print( program() )
        repetition=input("Wanna play again - press 1")
