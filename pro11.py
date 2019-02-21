# Q 11] Modified run-length encoding.

from collections import Counter

L = ['a','b','c','a','d','c','a','c','a','d']
c = Counter(L)
lst1 = []
lst2 = []
result = []
for i,j in c.items():
    if(j == 1):
        result.append(i)
    else:
        lst1 = [i,j]
        lst2.append(lst1)
print (lst2)
lst3=[lst2,result]
print (lst3)
print ("result list:",result)


''' output
[['a', 4], ['c', 3], ['d', 2]]
[[['a', 4], ['c', 3], ['d', 2]], ['b']]
result list: ['b']

'''