# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def summa(num):
    return sum(map(int, num.replace('.','').replace('-','')))

num = input('input a number: ')
print(f'sum digits in number: {summa(num)}')