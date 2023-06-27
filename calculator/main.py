num1, num2, math = int(input()), int(input()), input()

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