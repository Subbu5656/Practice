print('&& overriding &&')
class A:
	def add(self,a,b):
		return a+b
class B:
	def mult(self,a,b):
		return a*b
a=A()
b=B()
print(a.add(10,20))
print(b.mult(20,1))
class D:
	def sub(self,b,c):
		return b-c
e=D()
print(e.sub(200,30))