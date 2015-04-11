import math

# to add two numbers
def add(a, b):
	return a + b

# to subtract two numbers
def subtract(a, b):
	return a - b

# to multiply two numbers
def multiply(a, b):
	return a * b

# to divide two numbers
def divide(a, b):
	return a / b

# get sine of an angle
def sine(a):
	return math.sin(a)

# get cosine of an angle
def cosine(a):
	return math.cos(a)

while(1):
	c = int(input('Enter your choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Sine\n6.Cosine\n7.Exit\n\nYour choice: '))
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
		print ("sin(%f) = %f\n" % (a, sine(a)))
	elif(c == 6):
		print ("cosine(%f) = %f\n", % (a, cosine(a)))
	elif(c == 7):
		break
	

