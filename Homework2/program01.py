'''Write a function stat(lst, first, last) that returns a list of length 
n = last - first + 1 such that its value at position k is the number of
occurrences of the integer first + k in the list lst. It is assumed that lst
is a list of integer and that first <= last. Example:

	stat([3, 0, 2, 78, 5, 3, 12, 10, 23, 7, 2, 12, 0, 10, 10], 6, 15) returns
		[0, 1, 0, 0, 3, 0, 2, 0, 0, 0]
'''

def CountListOccurrences ( lst, element ) :

	occurrences = 0	
	
	for obj in lst :
		
		if obj == element :
		
			occurrences += 1
	
	return occurrences

def stat(lst, first, last):

	newList = []
	
	for k in range ( last - first + 1 ) :
	
		newList.append ( CountListOccurrences ( lst, first + k ) )
	
	return newList

print stat([3, 0, 2, 78, 5, 3, 12, 10, 23, 7, 2, 12, 0, 10, 10], 6, 15)
