data = '''101 sai tcs hyd 35000
102 bubbu hcl bang 45000
103 vivek hp chennai 55000'''


employee_data = {line.split()[0]:{'name':line.split()[1],'company':line.split()[2],'place':line.split()[3],'salary':int(line.split()[4])} for line in data.splitlines()}
print(employee_data)
class Bank:
		def __init__(self, id):
			self.id = employee_data.get(id)
			print(self.id)
			self.salary=(self.id).get('salary')
			print(self.salary)
		def withdraw(self, amount):
			return self.salary-amount
			#print ("mr {} 10000 has deposited to your account.Total Balance is 47000."format('101'))
v=Bank('101')
print(v.withdraw(50000))




