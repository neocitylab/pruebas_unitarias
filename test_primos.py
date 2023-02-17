from funciones import primos

def test_primos():
	assert primos(2) == True
	assert primos(3) == True
	assert primos(5) == True
	assert primos(7) == True
	assert primos(11) == True
	assert primos(13) == True
	assert primos(15) == False
