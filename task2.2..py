import math
import re
def valid(numbers):
    return bool (re.match('\d',numbers))
def get_count(numb):
    number=input(numb)
    while not valid(number):
        number=input(numb)

    return int(number)
def program():
    x=get_count("Введіть x")
    return math.log2(x)

print("Неділько Дарина Вікторівна \n Лабораторна робота №2 \n Варіант 14 \n Завдання №2. ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print( program() )
        repetition=input("Wanna play again - press 1")

