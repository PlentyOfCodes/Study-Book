###MAP
numbers=[*range(1,6)]
print(numbers)

for i in range(5):
    numbers[i]=numbers[i]**2
print(numbers)

def square(x):
    return x**2
'''
with map function
'''
numbers=[*range(1,6)]
mapped_list=[*map(square,numbers)]
print(mapped_list)

###FILTER
def filter_even_num(x):
    if x%2==0: return x

### shorter version
def filter_even_num_V2(x):
    return x if x%2==0 else None

numbers=[*range(1,6)]
filtered_list=[*filter(filter_even_num,numbers)]
print(filtered_list)
### LAMBDA FUNCTION
#MAP
numbers=[*range(1,6)]
mapped_lambda=[*map(lambda x: x**2,numbers)]
print(mapped_lambda)

mapped_lambda=[*map(lambda x: x**2,[*range(1,6)])]

#FILTER
filter_lambda=[*filter(lambda x: x if x%2==0 else None,[*range(1,6)])]
print(filter_lambda)