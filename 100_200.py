number = int(input())

result = ''

if number < 100:
    result = 'Less than 100'
elif number > 200:
    result = 'Greater than 200'
else:
    result = 'Between 100 and 200'

print(result)