# Q 12]  Decode a run-length encoded list.

from collections import Counter

L = ['a','b','c','a','d','c','a','c','a','d']
cnt = Counter(L)
lst = []
lst2 = []
result = []
for i,j in cnt.items():
    if(j == 1):
        result.append(i)
    else:
        lst = [i,]*j
        lst2.append(lst)
print (lst2)

''' output 

[['a', 'a', 'a', 'a'], ['c', 'c', 'c'], ['d', 'd']]

'''