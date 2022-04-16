import random

"""
1. Напишите программу на Python для чтения
последних n строк файла. Количество последних строк принять от пользователя.
"""


def printLatLines(filename, n):
    with open(filename, 'r') as file:
        linesFromFile = file.readlines()

    # print(linesFromFile[-n:])
    text = ' '
    for textLines in linesFromFile[-n:]:
        text += textLines

    return text


'''
2. Напишите программу на Python для подсчета количества строк в текстовом файле.
'''


def countLines(filename):
    numLines = 0
    # counter = 0

    with open(filename, 'r') as file:
        line = file.readline()
        while line:
            line = file.readline()

            numLines += 1

    return numLines


'''
 Напишите программу на Python для чтения случайной строки из файла.
'''


def randLines(filename):
    lines = open(filename).read().splitlines()
    print(lines)

    return random.choice(lines)


'''
4. Примите от пользователя список из 10 работников. 
Запишите данный список в отдельный файл как workers.txt. 
Имена каждого из сотрудников должно быть в отдельной строке.
'''


def newText(listWorkers):
    with open('workers.txt', 'w') as file:
        # for worker in listWorkers:
        #     file.write('\n'.join(worker))
        # for line in listWorkers:
        file.write('\n'.join(str(line) for line in listWorkers))
        # file.write('\n')
        '''
        listNew = []
        for i in listWorkers:
        listNew.append('\n'.join(i))
        
        file.write(listNew)
        '''

    print('File successfully wrote!')


'''
Документ «article.txt» содержит следующий текст:
 
Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела
 
Требуется реализовать функцию longest_words(file), которая выводит слово, 
имеющее максимальную длину (или список слов, если таковых несколько).
'''

def longestWord():
    maxLenWord = ''

    with open('article.txt', 'r') as file:
        text = file.read()

    words = text.split()
    # print(text)
    # print(words)
    # print(max(words))
    # print(len(words))

    maxLen = 0
    for word in words:
        # print(len(words))
        if len(words) > maxLen:
            maxLen = len(word)

    for word in words:
        if len(word) == maxLen:
            maxLenWord = word

    return maxLenWord



def main():
    filename = 'sometext.txt'

    numLines = int(input('Please enter the number of rows to print: '))

    lastLines = printLatLines(filename, numLines)
    print(lastLines)

    numLines = countLines(filename)
    print(numLines)

    print(randLines('sometext.txt'))

# Task 4
    listWorkers = ['Nazgul', 'Roza', 'Jazgul', 'Sasha', 'Masha', 'Dariya', 'Sveta',
                   'Klara', 'Jack', 'Margo']
    newText(listWorkers)

    # Task 5
    maxLenWord = longestWord()
    print(maxLenWord)


if __name__ == '__main__':
    main()
