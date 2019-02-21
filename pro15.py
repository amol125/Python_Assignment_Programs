#Q:15 Duplicate the elements of a list a given number of times

def dupli(l1,num):
	temp=[]
	for i in l1:
		temp.append(i*num)
	output=[]
	for j in temp:
		output.extend(list(j))
	return output
l=['a','b','c','d']
x=int(input('enter the number :'))
print ('The duplicate list is:',dupli(l,x))

''' output 

enter the number :3
The duplicate list is: ['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd']

'''