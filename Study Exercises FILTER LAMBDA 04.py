'''
Using filter() function filter the list so that 
only negative numbers are left.'''
lst1=[12, -1, 9, 8, -0.5, -0.2, -100]
#Type your answer here.
lst2=list(filter(lambda x: x<0, lst1))
print(lst2)

'''
Using filter function, filter the even numbers 
so that only odd numbers are passed to the new list.'''
lst1=[22, 100, 19, 13, 11, 1, 4, 66]
#Type your answer here.
lst2=list(filter(lambda x: x%2==1,lst1))
print(lst2)

'''
Using filter() and list() functions 
and .lower() method filter all the vowels in a given string.'''

str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.
##Filter boolean degere atayip sonucu 1 olani aliyor, else mutlaka yazilmali yoksa hata veriyor
##None yerine False da yazilabili
##True yerine 3 gibi bir sayi da verilebilir
lst=list(filter(lambda x : True if x.lower() in "aeiou" else None,str1))
lst_2=[*filter(lambda x : True if x.lower() in "aeiou" else None,str1)]

print(lst_2)

'''
This time using filter() and list() functions filter all 
the non-negative integers in the string.

'''
str1="Winter Olympics in 2022 will take place in Beijing China"
#Type your answer here.
lst=list(filter(lambda x: True if x in "0123456789" else None, str1))
print(lst)

'''
Using map() and filter() functions add 2000 to the values below 8000.'''

lst1=[1000, 500, 600, 700, 5000, 90000, 17500]
#Type your answer here.
lst2=list(map(lambda x: x+2000, filter(lambda x:x<8000, lst1)))
print(lst2)

'''
This time swap the map() and filter() functions so that 
map() function is inside filter() function. 
Convert a number to positive if it's negative in the list. 
Only pass those that are converted from negative to positive to the new list.

'''

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
#Type your answer here.

lst2=list(map(lambda x: -x, filter(lambda x: True if x<0 else False,lst1)))
lst3=list(map(lambda x: -x, filter(lambda x: -x<0 ,lst1)))
lst4=list(filter(lambda x: True if x>0 else None, map(lambda x: x*-1, lst1)))
lst5=list(filter(lambda x: x>0 , map(lambda x: x*-1, lst1)))

print(lst3)
print(lst4)
print(lst2)




