#Q:14 Duplicate the elements of a list 

def dupli(l1):
	temp=[]
	for i in l1:
		temp.append(i*2)
	output=[]
	for j in temp:
		output.extend(list(j))
	return output
l=['a','b','c','d']
print ('the original list is:',l)
print ('The duplicate list is:',dupli(l))

''' output

the original list is: ['a', 'b', 'c', 'd']
The duplicate list is: ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd']


'''