#Q 3] program to find the kth element of a list

def find_ele(a,b):
    try:
        return a[b]
    except:
        print('list index out of Bound')
        

l1=[1,2,3,4]
print('The list is ',l1)
x=int(input('enter the index of element in list :'))
print(find_ele(l1,x))


""" Output

The list is  [1, 2, 3, 4]
enter the index of element in list :2
3

"""