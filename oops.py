class Maths():
	def add(self, a, b):
		return a+b
	def sub(self, a, b):
		return a-b
	def multiply(self, a, b):
		return a*b
	def divide(self, a, b):
		return a/b
	def floordiv(self, a, b):
		return a//b
	def modulus(self, a, b):
		return a%b
operators=Maths()
print(operators.add(6, 5))
print(operators.sub(13, 2))
print(operators.multiply(11, 1))
print(operators.divide(22, 2))
print(operators.floordiv(889, 8))
print(operators.modulus(90, 2))							