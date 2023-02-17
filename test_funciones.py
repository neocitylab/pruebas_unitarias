from funciones import sumar

def test_sumar():
	assert sumar(2, 4) == 6
	assert sumar(-2, 2) == 0
	assert sumar(3, 2) == 5
	
