import re
# contruimos la matriz a partir
# de un path proveido como parametro
def buildMatrix (path):
	file = open (path, 'r')
	matrix = [line.split() for line in file]
	
	file.close()
	return matrix

# convertirmos a binario un valor decimal.
# El tamaño del binario está definido por
# n_bit
def literalToBinary (lit, n_bit):
	if lit >= (2**n_bit):
		exit()

	binario = ''
	decimal = lit
	while decimal > 0:
		binario = str(decimal % 2) + binario
		decimal = decimal // 2

	return (str(decimal)* (n_bit-len(binario))) + binario

# obtenemos el binario que corresponde 
# al nombre del registro registro
def getRegFile_binary (c_a, r_f):
	for fila in range(len(r_f)):
		if r_f[fila][0] == c_a:
			return r_f[fila][1]

def deleteChar (matrix, char):
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			matrix[x][y] = re.sub("\\" + char, "", matrix[x][y])
		pass
	return matrix