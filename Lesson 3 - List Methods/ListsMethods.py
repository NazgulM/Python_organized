companies = ['Microsoft', 'Google', 'Oracle', 'Apple']
for item in companies:
    print(item)

print()
i = 0
while i < len(companies):
    print(companies[i])
    i +=1

companies.insert(4,'AMD')
print(companies)