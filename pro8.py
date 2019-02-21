#Q 8] program to Eliminate consecutive elements from list

l1=[1,1,1,2,3,4,4,5,6]
print ('list before :',l1)
i=0
while (i<len(l1)-1):
    if(l1[i]==l1[i+1]):
        del l1[i]
    else :
        i=i+1

print ('list after:',l1)

''' output
list before : [1, 1, 1, 2, 3, 4, 4, 5, 6]
list after: [1, 2, 3, 4, 5, 6]
'''