def sumar(x, y):
	return x + y
	
def primos(x):
	contador=0
	i=2
	if x < 2:
		return False
		
	for i in range(x):
		if x % i == 0:
			contador+=1
		
	if contador > 0:
		return False
	else:
		return True               
print(primos(8))
