userInfo = input('Please enter the name: ')
age = int(input("Please enter age: "))
address = (input('Address: '))
salary = int(input('Salary please: '))
with open('file.txt', 'w') as myfile:
    myfile.write(f'Name: {userInfo}, \nyour age: {age}, '
                 f'\naddress: {address} \nsalary : {salary}')

