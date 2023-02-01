"""
Using .sort() method, create a lambda function
that sorts the list in descending order. Refrain from using the reverse parameter.
(Hint: lambda will be passed to sort method's key parameter as argument)
Please check out Hint 0 below to
be informed about a glitch regarding this exercise"""
lst=[100, 10, 10000, 1, 9, 999, 99]
lst.sort(key=lambda x: -x)
print(lst)


'''
his time use the sorted() function 
to sort the list in ascending order with lambda.'''
lst=[100, 10, 10000, 1, 9, 999, 99]
lst_result=sorted(lst,key=lambda x: -x)
print(lst)

"""
Using sorted() function and lambda sort the words in the list
based on their second letter from a to z."""

lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
#Type your answer here.

lst=sorted(lst,key=lambda x: x[1])
print(lst)

"""
Using sorted() function and lambda 
sort the tuples in the list based on the second items."""
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
lst=sorted(lst,key=lambda x: x[1])
print(lst)

'''Using sorted() function and lambda sort the tuples in the list 
based on the last character of the second items.

'''
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
lst=sorted(lst,key=lambda x: x[1][-1])
print(lst)

'''
Using sorted() function, reverse parameter and lambda sort the tuples in the list 
based on the last character of the second items in reverse order.'''

lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
#Type your answer here.
lst=sorted(lst,key=lambda x: x[1][-1], reverse=True)
print(lst)


