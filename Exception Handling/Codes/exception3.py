class FormulaError(Exception): pass

def length_check(lst) :
	try :
		if len(lst)!=3 :
			raise FormulaError("Invalid number of elements")
			return FormulaError
	except :
		print("Invalid number of elements")
		return FormulaError("Invalid number of elements")

def evalute(lst) :
	try :
		a = float(lst[0])
		b = float(lst[2])
	except :
		print("Invalid operands")
		return FormulaError("Invalid operands")
	try :
		if lst[1] == '+':
			val = a+b
			return val
		elif lst[1] == '-' :
			val = a-b
			return val
		else :
			print("Invalid operator")
			return FormulaError("Invalid operator")
	except :
		print("Invalid operator")
		return FormulaError("Invalid operator")

while True:
	exp = input("Enter the expression(type quit to terminate) : ")
	if exp=="quit" :
		exit(1)
	lst = exp.split()
	if length_check(lst) != FormulaError :
		val = evalute(lst)
		print(val)
			


















