from modAvl_Class import *

#Reading file data
def enter():
	f = open('input.txt')
	string = f.readlines()
	f.close()
	l_insert = []
	l_delete = []
	NI = string[0]
	ND = string[2]
	
	for val in string[1].split():
		l_insert.append(int(val))
	
	for val in string[3].split():
		l_delete.append(int(val))
		
	return l_insert,l_delete, int(NI), int(ND)
	
l_insert,l_delete, NI, ND = enter()

print l_insert
print l_delete

root = avlNode(l_insert[0])
for i in range(1,NI):
	root.avl_insert(l_insert[i])

print "The inserted tree is as follows : \n"
root.avl_print()

for i in range(ND):
	root.avl_delete(l_delete[i])
	print "After deleting the number {0} : \n".format(l_delete[i])
	root.avl_print()

print "\nThe pre-order traversal is : \n"
root.preorder()
