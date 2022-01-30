class ModelA:

	def __init__(self):
		self.gas = 100

	def run(self):
		self.gas = self.gas - 5

	def charge(self,supplu_amount):
		self.gas = self.gas + suppy_amount
		pring("現在のガソリンは{}リットルです".format(self.gas))

model_A = ModelA()
model_A.run()
print(model_A.gas)

class ModelA_2:
	def __init__(self,gas):
		self.gas = gas

	def run (self):
		print("10km走りました")

	def charge(self,supply_amount):
		self.gas = self.gas + supply_amount
		print("現在のガソリンは{}リットルです".format(self.gas))

model_A_2 = ModelA_2(200)
model_A_2.gas

class Human:

	def __init__(self):
		self.health = 100

	def time(self):
		self.time = 10

	def achieve(self):
		self.achieve = 0

	def work(self):
		print("work")
		self.achieve += 1
		self.time -= 1
		self.health -= 50

	def rest(self):
		print("rest")
		self.time -= 3
		self.health += 50

class ModelB(ModelA):
	def turbo(self):
		self.gas = self.gas-10
		print("ターボ機能を発動します！")

model_B = ModelB()
model_B.run()
model_B.turbo()
print(model_B.gas)
