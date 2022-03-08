from functions import literalToBinary, getRegFile_binary

# formato de código máquina y cantidad de bits correspondientes
# tj
# | opcode | index |
# | 6      | 26    |

class TypeJ:
	def __init__(self):
		super(TypeJ, self).__init__()
		# variables de estados
		self.iset = []
		self.code_assemb  = []
		self.reg_file 	 = []
		self.code_machine = []
		# variables de formato
		self.opcode		= []
		self.index		= []

	# Seteamos la variables de estado
	def setTypeJ (self, mips, reg_f, c_asm ):
		self.clearAll()
		self.iset 		 = mips [2 : len(mips)].copy()
		self.code_assemb = c_asm[1 : len(c_asm)].copy ()
		self.reg_file 	 = reg_f.copy()
	# realizamod la conversion de codigo assembler
	# a código maquina
	def convert (self):
		j = 0
		count = 1
		for pto in self.iset:
			if pto == "ind":
				self.index = [literalToBinary (int(str(self.code_assemb [j])), 26)]
				j += 1
			else:
				if count == 1:
					self.opcode.append (pto)
			count = count + 1

		self.setCodeMachine ("".join(self.opcode))
		self.setCodeMachine ("".join(self.index))
		
		return self.getCodeMachine ()
		
	# Se limpian todas las matricex y arrays
	def clearAll (self):
		if len(self.code_assemb) != 0:
		 	self.code_assemb.clear ()
		if len(self.code_machine) != 0:
			self.code_machine.clear ()
		if len(self.iset) != 0:
			self.iset.clear ()
		if len(self.opcode) != 0:
			self.opcode.clear ()
		if len(self.index) != 0:
			self.rd.clear ()

	def getISet (self):
		return self.iset
		
	def getRegFile (self):
		return self.reg_file
		
	def getCodeAssembler (self):
		return self.code_assemb

	def setCodeMachine (self, arg):
		self.code_machine.append (arg)

	def getCodeMachine (self):
		return self.code_machine
