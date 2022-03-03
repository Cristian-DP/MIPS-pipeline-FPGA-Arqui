
# contruimos la matriz a partir
# de un path proveido como parametro
def buildMatrix (path):
	file = open (path, 'r')
	matrix = [line.split() for line in file]
	
	return matrix

