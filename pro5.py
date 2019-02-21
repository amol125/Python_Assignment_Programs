# Q 6] program to find whether a list is palindrome

## function
def palindrome(a):
    print (a)
    l2=a[::-1]
    if(a==l2):
        print ('list is palindrome')
    else:
        print ('list is not palindrome')
## driver code
l1=[1,2,3,4]
palindrome(l1)
l=[1,2,1]
palindrome(l)


'''
  Output

  [1, 2, 3, 4]
list is not palindrome
[1, 2, 1]
list is palindrome

'''