# open() - open files and work with them
# close() - close all operations
# read() - read the file
# write() - writing this files
"""
Regimes:
r- read files
w - write new files
a - adding content to files
b - binary files
"""
# myFile = open('info.txt', 'w')
# myFile.close()

try:
    myFile = open('info2.txt', 'r')
    try:
        print('Hello file doing well')
    except:
        print('Some error')
    finally:
        myFile.close()
except FileNotFoundError:
    print('Cannot open a file')

with open('info.txt', 'r') as myfile:
    print('Hello file doing well')

with open('inf02.txt', 'w') as myFile2:
    myFile2.write('''
    I am learning Python this morning 
    in Bishkek thru ZOOM application and its awesome
    ''')
print('code...')

# infoUser = input('Please enter your text!: ')
#
# with open('info3.txt', 'w') as myFile3:
#     myFile3.write(infoUser)

with open('info.txt', 'w') as myFile4:
    myFile4.write('\nNew  content')

with open('inf02.txt', 'a') as myFile5:
    myFile5.write('\nUpdate the content')

# with open('info3.txt', 'a') as myFile6:
#     myFile6.write(f'- {infoUser}')

with open('inf02.txt', 'w') as myFile5:
    myFile5.write('''I am learning Python this morning 
    in Bishkek thru ZOOM application 
    and its awesome''')

with open('inf02.txt', 'r') as rfile:
    line1 = rfile.readline()
    line2 = rfile.readline()
    textfile = rfile.read()
print(line1)
print(line2)
print(textfile)

with open('inf02.txt', 'r') as rfile:
    for line in rfile:
        print(line, end=' ')

sometext =' '
with open('inf02.txt', 'r') as rfile:
    for line in rfile:
        sometext+=line
print(sometext)



with open('inf02.txt', 'r') as rfile2:
    line = rfile2.readline()

    while line:
        print(line, end=' ')
        line = rfile2.read()

print()
with open('inf02.txt', 'r') as rfile3:
    contents = rfile3.readlines()

print(contents)
line1 = contents[0]
print(line1)
line2 = contents[2]
print(line2)