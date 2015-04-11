def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

while(1):
	c = int(input('Enter your choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Exit\n\nYour choice: '))
	a = float(input('Enter first operand'))
	b = float(input('Enter second operand'))

	if(c == 1):
		print ("%f + %f = %f\n" % (a, b, add(a, b)))
	elif(c == 2):
		print ("%f - %f = %f\n" % (a, b, subtract(a, b)))
	elif(c == 3):
		print ("%f * %f = %f\n" % (a, b, multiply(a, b)))
	elif(c == 4):
		print ("%f / %f = %f\n" % (a, b, divide(a, b)))
	elif(c == 5):
		break

