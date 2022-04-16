with open('lorem.txt', 'w') as myfile:
    myfile.write('''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem
Ipsum has been the industry's standard dummy text ever since the 1500s, when an
unknown printer took a galley of type and scrambled it to make a type specimen
book. It has survived not only five centuries, but also the leap into electronic
typesetting, remaining essentially unchanged. It was popularised in the 1960s with
the release of Letraset sheets containing Lorem Ipsum passages, and more recently
with desktop publishing software like Aldus PageMaker including versions of Lorem
Ipsum.
    ''')

with open('lorem.txt', 'r') as myFile:
    lines = myFile.readline()

    while lines:
        print(lines, end=' ')
        lines = myFile.read()

with open('lorem.txt', 'r') as myFile:
    text = myFile.read()
print(text)

with open('lorem.txt', 'r') as myFile:
    list1 = myFile.readlines()
    print(list1)

print()
# 2. Прочтите текст из задания 1 в обратном порядке
with open('lorem.txt', 'r') as myFile:
    list2 = myFile.readlines()
    for line in reversed(list2):
        print(line)

# Other way
with open('lorem.txt', 'r') as myFile:
    text = myFile.read()
    revText = text[::-1]
    print(revText)

'''
Создайте программу, в котором будет записывать введенный пользователем массив строк 
(Линию строк) и считывать его обратно из файла на консоль.
'''
someText = input('Please enter some words: ')

with open('msg.txt', 'w') as file:
    file.write(someText)

with open('msg.txt','r') as file:
    print(someText)