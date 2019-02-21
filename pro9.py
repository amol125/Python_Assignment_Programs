# Q 9] Pack consecutive duplicates of list elements into sublists.

from collections import Counter

l1 = [1,2,3,3,1,4,2,4,2,5,5,2,5,5]
c = Counter(l1)
print ('list before:',l1)
print ('list after:',[ [i,]*j for i,j in c.items()])



''' Output

list before: [1, 2, 3, 3, 1, 4, 2, 4, 2, 5, 5, 2, 5, 5]
list after: [[1, 1], [2, 2, 2, 2], [3, 3], [4, 4], [5, 5, 5, 5]]

'''