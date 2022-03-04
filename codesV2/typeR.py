from functions import literalToBinary, getRegFile_binary
import re

# formato de código máquina y cantidad de bits
# correspondientes
# | opcode | rs | rt | rd | sa | function |
# | 6      | 5  | 5  | 5  | 5  | 6        |

class TypeR:
	def __init__(self):
		super(TypeR, self).__init__()
		# variables de estados
		self.iset = []
		self.code_assemb  = []
		self.reg_file 	 = []
		self.code_machine = []
		# variables de formato
		self.opcode		= []
		self.rs			= []
		self.rd			= []
		self.rt			= []
		self.sa 		= []
		self.function	= []

	# Seteamos la variables de estado
	def setTypeR (self, mips, reg_f, c_asm ):
		self.clearAll()
		self.setISet (mips [2 : len(mips)])
		self.setCodeAssembler (c_asm[1 : len(c_asm)])
		self.setRegFile (reg_f)
	# realizamod la conversion de codigo assembler
	# a código maquina
	def convert (self):
		j = 0
		count = 1
		for pto in self.iset:
			if pto == "rd":
				self.rd = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "rs":
				self.rs = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "rt":
				self.rt = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "sa":
				self.sa = [literalToBinary (int(str(self.code_assemb [j])), 5)]
				j += 1
			else:
				if count == 1:
					self.opcode.append (pto)
				if count == 2:
					self.rs.append (pto)
				if count == 3:
					self.rd.append (pto)
				if count == 4:
					self.rt.append (pto)
				elif count == 5:
					self.sa.append (pto)
				elif count == 6:
					self.function.append (pto)
			count = count + 1

		self.setCodeMachine ("".join(self.opcode))
		self.setCodeMachine ("".join(self.rs))
		self.setCodeMachine ("".join(self.rt))
		self.setCodeMachine ("".join(self.rd))
		self.setCodeMachine ("".join(self.sa))
		self.setCodeMachine ("".join(self.function))
		
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
		if len(self.rd) != 0:
			self.rd.clear ()
		if len(self.rs) != 0:
			self.rs.clear ()
		if len(self.rt) != 0:
			self.rt.clear ()
		if len(self.sa) != 0:
			self.sa.clear ()
		if len(self.function) != 0:
			self.function.clear ()

	def setISet (self, arg):
		self.iset = arg.copy()

	def getISet (self):
		return self.iset
	
	def setRegFile (self, arg):
		self.reg_file = arg.copy()
		
	def getRegFile (self):
		return self.reg_file

	def setCodeAssembler (self, arg):
		self.code_assemb = arg.copy ()
		
	def getCodeAssembler (self):
		return self.code_assemb

	def setCodeMachine (self, arg):
		self.code_machine.append (arg)

	def getCodeMachine (self):
		return self.code_machine
