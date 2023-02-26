'''l=[1,2,3,4,5,6]
even=[]
for i in l:
	if i%2==0:
		print(i)
	even.append(i)
print(even)
odd=[]
for i in l:
	if i%2==1:
		print(i)
	odd.append(i)
print(odd)
'''
'''def add (a,b):
	c=a+b
	return c
print (add (10,20))
'''

s= '123a45'
count=0
for i in s:
	if i.isdigit():
		count=count+int(i)
		print(count)
		





