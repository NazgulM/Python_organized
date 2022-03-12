# adding elements to the list
myListNumber = list(range(7,45,7))
myListString = ['Timur', 'Oleg', 'Asan', 'Elena', 'Alena', 'Aisuluu']
print(myListNumber)

myListNumber.append(100) # adding elements to the end of the list
print(myListNumber)

myListString.append('Stepan')
print(myListString)


# Adding to certain position
myListNumber.insert(1, 50)
print(myListNumber) # 14 goes to the right

myListString.insert(3, 'Murat')
print(myListString)

myListNumber = list(range(7,45,7))
myListString = ['Timur', 'Oleg', 'Asan', 'Elena', 'Alena', 'Aisuluu']

# Delete from the end
myListNumber.pop()
print(myListNumber)

myListString.pop()
print(myListString)

# delete from the end with index
myListNumber.pop(1)
print(myListNumber)

myListString.pop(2)
print(myListString)

# Delete with remove
myListNumber = list(range(7,45,7))
# [7, 14, 21, 28, 35]

myListNumber.remove(35)
print(myListNumber)

myListString = ['Timur', 'Oleg', 'Asan', 'Elena', 'Alena', 'Aisuluu']
myListString.remove('Timur')
print(myListString)

# index() count ()  clear ()
myListNumber = list(range(7,45,7))
myListNumber.clear()
print(myListNumber)

# without index delete all list
# del myListNumber[2]
# print(myListNumber)

# index to know number of list
myListString = ['Timur', 'Oleg', 'Asan', 'Elena', 'Alena', 'Aisuluu']
print(myListString.index('Alena'))

# count
myListString = ['Timur', 'Oleg', 'Asan', 'Elena', 'Alena', 'Aisuluu', 'Asan', 'Timur']
print(myListString.count('Timur'))