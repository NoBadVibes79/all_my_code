flag = input(
    'Хочешь ли ты что-то посчитать? Да или нет: ')

while flag != 'нет':
    num1, num2, math = int(input('Введи первое число: ')), int(
        input('Введи второе число: ')), input('Введи операцию вычисления: ')
    if math == '+':
        print(num1 + num2)
    elif math == '*':
        print(num1 * num2)
    elif math == '-':
        print(num1 - num2)
    elif math == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print('На ноль делить нельзя!')
    else:
        print('Неверная операция')
    flag = input(
        'Хочешь ли ты что-то посчитать? да или нет: ')
