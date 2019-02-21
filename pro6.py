#Q 6] program to reverse the list in python

def rev(a):
    newlist=a[::-1]
    return newlist

l1=[1,2,3,4]
print('list before:',l1)
print ('list after:',rev(l1))


''' output
list before: [1, 2, 3, 4]
list after: [4, 3, 2, 1]

'''

