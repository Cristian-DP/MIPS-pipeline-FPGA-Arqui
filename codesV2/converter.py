from typeR import TypeR
from typeI import TypeI
from typeJ import TypeJ
from functions import buildMatrix, deleteChar

# determina si el jalr a utilizar corresponde al
# jarl del código assembler
def jalr (c_a, m):
	if "jalr" not in m:
		return 1

	cant_reg = len(c_a) - 1
	if (cant_reg == 1 and "rd" not in m):
	 	return 1
	elif (cant_reg == 2 and "rd" in m):
		return 1

	return 0

# path
path = "examplesCode/sw.asm"
# variables para el codigo assembler 
codeMachine_file = open ("codeMachine.mem", "a")
c_asm = []

# objetos de tipos de intrucciones
type_r = TypeR ()
type_i = TypeI ()
type_j = TypeJ ()

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
			# determino jalr
			ret = jalr (code_assembler[pto_asm], mips [pto_mips]) 
			if ret != 0:
				# opcion tr
				if mips [pto_mips][1] == "tr":
					type_r.setTypeR(mips[pto_mips], register_file, code_assembler[pto_asm])
					c_asm = type_r.convert ()
				# opcion tim
				elif mips [pto_mips][1] == "tim" or mips [pto_mips][1] == "tio" or mips [pto_mips][1] == "tib":
					type_i.setTypeI(mips[pto_mips], register_file, code_assembler[pto_asm])
					c_asm = type_i.convert ()
				elif mips [pto_mips][1] == "tj":
					type_j.setTypeJ(mips[pto_mips], register_file, code_assembler[pto_asm])
					c_asm = type_j.convert ()

				codeMachine_file.write ("".join(c_asm) + "\n")
				
				print("convert " + str(code_assembler[pto_asm]) + " -> " + str(c_asm) )
				c_asm.clear()
codeMachine_file.close ()


