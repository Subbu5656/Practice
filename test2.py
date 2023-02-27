print('&& overloading &&')
def sub(a,b=0,c=0):
	return a-b-c
print(sub(10,20,30))
print(sub(20,30))
print(sub(40))


def add(a,b=0,c=0):
	return a+b+c
print(add(10,20,30))
print(add(20,30))
print(add(40))

