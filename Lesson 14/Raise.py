num1 = None
num2 = None
result = None

try:
    num1 = int(input('Num1: '))
    num2 = int(input('Num2: '))

    if num1 <= 0:
        raise Exception('First number should be greater than 0')
    elif num2 <= 0:
        raise Exception('Second number should be greater than 0')

    result = num1 / num2

except ValueError:
    print('Please enter the number')
except TypeError:
    print('Dividing error')
except ZeroDivisionError:
    print('Dividing to 0!')
except Exception as e:
    print('You did error! ', e)
finally:
    print(f'Result: {result}')
