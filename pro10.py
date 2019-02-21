# Q 10] Run-length encoding of a list.

from collections import Counter

l=['a','b','c','a','d','b','c']
c=Counter(l)
print ('list before:',l)
print('list after',[[i,j]for i,j in c.items()])

''' output

list before: ['a', 'b', 'c', 'a', 'd', 'b', 'c']
list after [['a', 2], ['b', 2], ['c', 2], ['d', 1]]

'''

