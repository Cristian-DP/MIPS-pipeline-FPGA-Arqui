from typeR import TypeR
from functions import buildMatrix, deleteChar

# variables para el codigo assembler 
codeMachine_file = open ("codeMachine.mem", "a")
c_asm = []

# objetos de tipos de intrucciones
type_r = TypeR ()

# construimos las matrices de los archivos
# con privilegio de lectura
register_file 	= buildMatrix ("register-file.txt")
code_assembler  = deleteChar ( buildMatrix ("assembler.asm"), "," )
mips			= buildMatrix ("mips.txt")

# se toma cada fila de la matriz de codigo asembler
# y la matriz de instrucciones,
# Se evalúa el tipo de instrucciones a la que pertenece.
# Se hace uso del objeto tipo de intrucciones para que
# realice la conversion
for pto_asm in range(len(code_assembler)):
	for pto_mips in range (len(mips)): 
		if code_assembler[pto_asm][0] ==  mips [pto_mips][0]:
			if mips [pto_mips][1] == "tr":
				c_asm = type_r.setTypeR(mips[pto_mips], register_file, code_assembler[pto_asm])
				codeMachine_file.write ("".join(c_asm) + "\n")
				c_asm.clear()
				break

codeMachine_file.close ()