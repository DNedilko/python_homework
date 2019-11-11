
import re
def valid(numbers):
    return bool (re.match('\d',numbers))
def get_count(numb):
    number=input(numb)
    while not valid(number):
        number=input(numb)
    return int(number)
def program():
    mn = get_count("Введіть кількість множників")
    x=get_count("Введіть x")
    function=1
    for numb in range(1, mn + 1):
        function = function * (x + 1) ** 2 / x

    return function
print("Неділько Дарина Вікторівна \n Лабораторна робота №1 \n Варіант 14 \n Завдання №3. Розв&#39;язування рівнянь за певної умови(х): якщо х<=13, то виконується рівність -х^3+9, якщо ж х>13, то виконується рівність -3/(x+1) ")
repetition=input("If you wanna play - press 1")
while repetition=="1":
        print( program() )
        repetition=input("Wanna play again - press 1")

