import math

data = {
    'a': 42,
    'b': {
        'ba': 23,
        'bb': {
            'bba': 420
        }
    }
}


def recursive_lookup(k, d):
    if k in d:
        return d[k]
    for v in d.values():
        if isinstance(v, dict):
            return recursive_lookup(k, v)
    return None


print('a', recursive_lookup('a', data))
print('ba', recursive_lookup('ba', data))
print('bba', recursive_lookup('bba', data))
print()

numbers = []

for i in range(1,6):
    numbers.append(2**i)
print(numbers)

for i in range(1,3):
    numbers.append(2**i)
print(numbers)

numbers2 = []

for i in range(1,4):
    numbers2.append(2**i)
print(numbers2)

numbers3 = []

for i in range(1, 4):
    numbers3.append(3**i)
print(numbers)

numbers4 = [4**i for i in range(1,5)]
print(numbers4)

numbers5 = [49, 64, 81, 100, 121]
new_list = [math.sqrt(n) for n in numbers5]
print(new_list)

numbers6 = [21, 64, 81, 100, 121, 16, 56]
new_list2 = [math.sqrt(n) for n in numbers6 if n % 2 == 0]
print(new_list2)

team1 = ['Janet', 'Arya', 'Mary']
team2 =['Evan', 'Jake', 'Randy']

new_list3 = [(x,y) for x in team1 for y in team2]
print(new_list3)

word = 'programming'
alphabet = {x for x in word}
print(alphabet)

numbers = [1, 2, 3, 4, 5]
square_dict = dict()

for num in numbers:
    square_dict[num] = num**2
print(square_dict)

numbers1 = [1, 2, 3, 4, 5]
sq_dict = {num: num**2 for num in numbers1}
print(sq_dict)

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

new_price = {key: value*1.5 if value > 2 else value for (key, value) in old_price.items()}
print(new_price)