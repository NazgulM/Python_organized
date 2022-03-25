
# String methods of collection
# Method split () - Разделение на подстроки
text = 'I love programming and its cool'
listSome = list(text)
print(listSome)

splitted_text = text.split()
print(splitted_text)

text2 = 'I live in Bishkek. I am 30 years old. My profession is programming.'
listText = text2.split('.')
print(listText)

text3 = 'I live in Bishkek, I am 30 years old, My profession is programming.'
listText3 = text3.split(',')
print(listText3)

text4 = text3.split(' ',2)
print(text4)

text5 = 'I, live, in, Bishkek, I, am, 30, years, old, My, profession, is, programming.'
listText4 = text5.split(',', 3)
print(listText4)

# Join() method

listText2 = text5.split(',')
print(listText2)

myText = ' '.join(listText2)
print(myText)
print(type(myText))

text2 = 'I live in Bishkek. I am 30 years old. My profession is programming.'

newText = '#'.join(text2)
print(newText)

