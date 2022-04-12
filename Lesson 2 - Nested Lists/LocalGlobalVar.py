def add_numbers(n1, n2):
    result = n1 + n2
    return result


print(add_numbers(2, 5))

message = 'How are you doing?'


def greet():
    message = 'How are you?'
    print('Message inside function: ', message)


greet()
print('Message outside function: ', message)

numbers = [1, 5, 6, -4]
print(numbers)
print(len(numbers))

#mixed list
random_list = [2.5, 'Hello', -5, 2.5]
print(random_list)

# empty list
list1 = []
print(len(list1))

languages = ['Python', 'Javascript', 'C++', 'Kotlin']
print(languages)
print(languages[0])
print(languages[2])

# negative indexing - gives items from the last
print(languages[-1])
print(languages[-3])

print(languages[0:3]) # slicing first index is inclusive and last is exclusive
print(languages[1:4])
print(languages[:3])
print(languages[1:])

# change second element
languages[1] = 'Ruby'
print(languages)

# changes 1,2 elements
languages[1:3] = ['Ruby', 'Dart']
print(languages)

print('Python' in languages)
print('Rust' in languages)
print()
# iterating through in the list
for language in languages:
    print(language)

# add Rust to list
languages.append('Rust')
print(languages)

languages.insert(1, 'Java')
print(languages)

languages.remove('Kotlin')
print(languages)

languages1 = languages.copy()
print(languages1)

# Tuples in Python, cannot be change

numbers = (21, -5, 6, 9)
print(numbers)
print(type(numbers))
print(numbers[2])
print(numbers[1:4])
print()
for number in numbers:
    print(number)

languages = ('Python', 'Javascript', 'C++', 'Kotlin')
print(languages)

