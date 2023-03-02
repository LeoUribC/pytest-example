def add(a,b):
	return a+b

def substract(a, b):
	return a-b

def test_add():
	assert add(0.1, 0.2) >= 0.3
	assert add("space", "ship") == "spaceship"
"""
def test_substract():
	assert substract(1, 2) == -1
"""
