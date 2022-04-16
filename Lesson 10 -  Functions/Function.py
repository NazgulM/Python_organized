#Ключевое слово return

def findSum(num, num2):
    print(f'Сумма двух элементов: {num + num2}')

def findMultiply(num, num2, num3, num4):
    result = num * num2 * num3 * num4
    print(f'Результат умножения: {result}')

def findSum2(num1, num2):
    #result = num1 + num2
    return num1 + num2

def findMultiply2(num, num2, num3, num4):
    #result = num * num2 * num3 * num4
    return num * num2 * num3 * num4

def print_list(sList):
    someListDoubled = []
    for i in sList:
       someListDoubled.append(i*2)
    return someListDoubled

def checkAge(age):
    resultAge = ''
    if age >=18:
        resultAge = 'You are adult!'
        return resultAge
    else:
        resultAge = 'You are too young!'
        return resultAge

someNum = 10

result = findSum2(20,30)  +  someNum
print(result)

result2 = findMultiply2(2,3,4,2)  +  someNum
print(result2)

someNum2 = findSum2(2,3)
print(someNum2)

someNum3 = findMultiply2(4,23,1,4)
print(someNum3)

myList = list(range(5,10))
print(print_list(myList))

newList = list(print_list(myList))
print(print_list(newList))


resultAge = 'Result: ' + checkAge(25)
answer = checkAge(15)
print(resultAge)
print(answer)
