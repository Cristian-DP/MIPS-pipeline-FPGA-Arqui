from typeR import TypeR
from typeI import TypeI
from functions import buildMatrix, deleteChar

# path
path = "examplesCode/suma.asm"
# variables para el codigo assembler 
codeMachine_file = open ("codeMachine.mem", "a")
c_asm = []

# objetos de tipos de intrucciones
type_r = TypeR ()
type_i = TypeI ()

# construimos las matrices de los archivos
# con privilegio de lectura
register_file 	= buildMatrix ("register-file.txt")
code_assembler  = deleteChar ( buildMatrix (path), "," )
mips			= buildMatrix ("mips.txt")

# se toma cada fila de la matriz de codigo asembler
# y la matriz de instrucciones,
# Se evalúa el tipo de instrucciones a la que pertenece.
# Se hace uso del objeto tipo de intrucciones para que
# realice la conversion
for pto_asm in range(len(code_assembler)):
	for pto_mips in range (len(mips)): 
		if code_assembler[pto_asm][0] ==  mips [pto_mips][0]:
			# opcion tr
			if mips [pto_mips][1] == "tr":
				type_r.setTypeR(mips[pto_mips], register_file, code_assembler[pto_asm])
				c_asm = type_r.convert ()
			# opcion tim
			elif mips [pto_mips][1] == "tim" or mips [pto_mips][1] == "tio":
				type_i.setTypeI(mips[pto_mips], register_file, code_assembler[pto_asm])
				c_asm = type_i.convert ()

			codeMachine_file.write ("".join(c_asm) + "\n")
			c_asm.clear()
codeMachine_file.close ()