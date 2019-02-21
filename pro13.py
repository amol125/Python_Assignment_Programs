# Q.13 Run-length encoding of a list (direct solution).

from collections import Counter

l= ['a','b','c','a','d','c','a','c','a','d']
c = Counter(l)
#lst1 = []
lst2 = []
result = []
for i,j in c.items():
    lst2.append(i)
print (l)
print (lst2)

''' output

['a', 'b', 'c', 'a', 'd', 'c', 'a', 'c', 'a', 'd']
['a', 'b', 'c', 'd']

'''
