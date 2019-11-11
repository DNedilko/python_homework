
def get_line_with_symbol(leters, symbol, line):
    linereplaced=line.replace(leters, symbol)
    return linereplaced, symbol
def get_symbols_counted(massive):
    linereplaced=massive[0]
    symbols=massive[1]
    amount=str(linereplaced.count(symbols))
    return ("У стрічці'"+ linereplaced + "' "+ amount + " символів '"+ symbols+"'")

leters=input("Введіть символи, які ви хочете замінити")
symbol=input("Введіть спеціальний символ на якиm ви хочете замінити символи "+ leters)
line=input("Введіть стрічку у якій ви хочете замінити ці слова")
print(get_symbols_counted(get_line_with_symbol(leters, symbol, line)))