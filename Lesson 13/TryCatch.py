age = int(input('Age: '))
print(age)
print('Continue of our program')

try:
    age = int(input('Age: '))
    print(age)

except:
    print('You are trying enter not number')

print('Continue of our program')
number1 = 0
number2 = 0

result = 0
try:
    number1 = int(input('Number1: '))
    number2 = int(input('Number2: '))
    result = number1//number2

    print(result)
except ZeroDivisionError as ze:
    print('You are trying to divide to 0')
except ValueError as ve:
    print('You entered string value')
except:
    print('Another error')
finally:
    print(f'Result is: {result}')

print('Continue of the program...')

listPeople = ['Adam', 'Petr', 'Stepan', 'Alena']

try:
    numberIndex = int(input('Enter the number of index: '))
    print(listPeople[numberIndex])

except IndexError as ie:
    print('You entered out of range of index!\nPlease try one more time')

    try:
        numberIndex = int(input('Enter the number of index: '))
        print(listPeople[numberIndex])

    except IndexError as ie:
        print('You entered out of range of index!')
print(listPeople)

someDict = {v:v*2 for v in range(1,11)}
print(someDict)

try:
    print(someDict[9])
except KeyError:
    print('No this key')

contactPerson = {
    'Askar': '0555343434',
    'Petr': '0777343434',
    'Aisuluu': '0555555555'
}
try:
    nameSearch = input('Please enter the name: ')
    print(contactPerson[nameSearch])
except KeyError:
    print('Can not find this contact person')
print('Code..')

try:
    number1 = int(input('Number1: '))
    number2 = int(input('Number2: '))
    result = number1 // number2
    print(listPeople[5])

except (ZeroDivisionError, ValueError):
    print('Вы пытались делить на Ноль!')
    print('ИЛИ Вы ввели строковое значение!')

except IndexError:
    print('Выход за пределы массива!')

except BaseException as be:
    print(f'Ошибка! Тип ошибки: {be}')

print('Продолжение программ.. остальной код')

