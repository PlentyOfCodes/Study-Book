
nums=[3,2,6,8,4,6,2,9]

#FILTER
evens=[*filter(lambda x: x if x%2==0 else None,nums)]
evens_2=[*filter(lambda x: x%2==0,nums)]
print(evens),print(evens_2)

#MAP
doubles=[*map(lambda x: x*2,nums)]
print(doubles)

#REDUCE
from functools import reduce
sum_list=reduce(lambda a,b: a+b ,[*range(5)])
print("sum list\n",sum_list)

factor_list=reduce(lambda a,b: a*b ,[*range(1,6)])
print("factor list\n",factor_list)