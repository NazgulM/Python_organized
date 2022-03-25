# Создание лямбда функции
def helloSay():
    print('Hello my dear friend!')


def helloSay2(name):
    print(f'Hello {name}!')


def addNumsThree(num1, num2, num3):
    return num1 + num2 + num3


def mathOperation(n1, n2, n3, operation):
    result = operation(n1, n2, n3)

    return result


def main():
    # sayHello = lambda: print('Hello my dear friend!')
    #
    # sayHello()
    # sayHello()
    #
    # helloSay()
    #
    # sayHello2 = lambda name: print(f'Hello {name}!')
    # sayHello2('Samat')
    #
    # addThreeNums = lambda n1, n2, n3: n1 + n2 + n3
    #
    # print(addThreeNums(34, 54, 65))
    #
    # result = 100 + addThreeNums(34, 54, 65)
    # print(result)
    #
    # print(addNumsThree(23, 43, 65))
    #
    # findAvg = lambda listMy: sum(listMy) / len(listMy)
    #
    # print(findAvg([34, 54, 65, 76, 76]))
    #
    # # 1 - Finding avg among three nums
    # avgResult = mathOperation(12, 43, 54, lambda num1, num2, num3: (num1 + num2 + num3) / 3)
    # print(avgResult)
    #
    # # 2 - Finding sum among three nums
    # sumThreeNUms = mathOperation(34, 435, 65, addThreeNums)
    # print(sumThreeNUms)
    #
    # # 3 - Finding multiply among three nums
    # multiplyResult = mathOperation(23, 43, 54, lambda num1, num2, num3: num1 * num2 * num3)
    # print(multiplyResult)

    # task 2
    # Создать лямбда выражение, которая возводит в квадрат переданное ей число
    square1 = lambda n: n * n
    print(square1(3))

    # task 3
    # Создать лямбду выражения, которая возвращает среднее значение среди 4 переданных чисел
    average = lambda n1, n2, n3, n4: ((n1 + n2 + n3 + n4) / 4)
    print(average(45, 3, 9, 8))

    # task 4
    # Примите от пользователя сумму для оплаты какого-нибудь товара.
    # В зависимости от того сколько платит покупатель,
    # необходимо будет провести расчеты через If Else конструкцию.
    # Необходимо произвести необходимые скидки по следующим критериям:
    # • Если сумма платы производится в промежутках от 1000 сом и до 1999
    # сом - выполнить скидку в 2%
    # • Если сумма платы производится в промежутках от 2000 сом и до 4999
    # сом - выполнить скидку в 5%
    # • Если сумма платы производится в промежутках от 5000 сом и до 9999
    # сом - выполнить скидку в 10%
    # • Если сумма платы производится в промежутках от 10 000 сом и выше -
    # выполнить скидку в 20% Пример вывода результата программы:

    sum = int(input('Please enter the payment: '))
    if 1000 <= sum <= 1999:
        findWithDiscount = lambda sum: sum - (sum * 0.02)
        print('Discount amount of 2.0% from 1000 KGS is: ', findWithDiscount(sum), 'KGS')
    elif 2000 <= sum <= 4999:
        findWithDiscount2 = lambda sum: sum - (sum * 0.05)
        print('Discount amount of 5.0% from 2000 KGS is: ', findWithDiscount2(sum), 'KGS')
    elif 5000 <= sum <= 9999:
        findWithDiscount3 = lambda sum: sum - (sum * 0.1)
        print('Discount amount of 10.0% from 5000 KGS is: ', findWithDiscount3(sum), 'KGS')
    elif sum >= 1000:
        findWithDiscount4 = lambda sum: sum - (sum * 0.2)
        print('Discount amount of 20.0% from 10000 KGS is: ', findWithDiscount4(sum), 'KGS')
    elif sum < 1000:
        print(f'Sorry we cannot give you discount for {sum} KGS')


if __name__ == '__main__':
    main()
