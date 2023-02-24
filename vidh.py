l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def even(l):
	if l%3==0:
		return l
print(list(filter(even,l)))
def odd(l):
	if l%5==0:
		return l
print(list(filter(odd,l)))