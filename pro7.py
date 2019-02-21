#Q 7] flatten a nested list structure

def flatten(l1,l2):
    for i in l1:
        for j in i:
            for k in j:
                l2.append(k)
                
    return l2

list1=['a',['b',['c','d'],'e']]
list2=[]
print ('List before :',list1)
print ('list after :', flatten(list1,list2))

''' ouput
List before : ['a', ['b', ['c', 'd'], 'e']]
list after : ['a', 'b', 'c', 'd', 'e']
'''