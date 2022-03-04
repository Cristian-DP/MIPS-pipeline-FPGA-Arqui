from functions import literalToBinary, getRegFile_binary
import re
# formato de código máquina y cantidad de bits correspondientes
# tim
# | opcode | rs | rt | inmediato |
# | 6      | 5  | 5  |  16       |
#
# tio
# | opcode | base	| rt | offset |
# | 6      | 5  	| 5  |  16    |

class TypeI:
	def __init__(self):
		super(TypeI, self).__init__()
		# variables de estados
		self.iset		 = []
		self.code_assemb = []
		self.reg_file 	 = []
		self.code_machine = []
		self.tipo 		= []
		# variables de formato
		self.opcode		= []
		self.rs			= []
		self.rt			= []
		self.inof		= []

	# Seteamos la variables de estado
	def setTypeI (self, mips, reg_f, c_asm ):
		self.clearAll()
		self.tipo 		 = mips[1:2]
		self.iset 		 = mips [2 : len(mips)].copy()
		self.code_assemb = c_asm[1 : len(c_asm)].copy ()
		self.reg_file 	 = reg_f.copy()

	# realizamod la conversion de codigo assembler
	# a código maquina
	def convert (self):
		if "tib" in self.tipo:
			return self.convertTib ()
		elif "tio" in self.tipo or "tim" in tipo:
			return self.convertTiom ()

	def convertTib (self):
		string = str(self.code_assemb[1:2])
		string = re.sub (r"\[|\'|\]|\)", "", string)
		string = re.split(r"\(", string)

		j = 0
		count = 1
		for pto in self.iset:
			if pto == "rt":
				self.rt = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "off":
				self.inof = [getRegFile_binary (string[1], self.reg_file)]
				j += 1
			elif pto == "base":
				self.rs = [literalToBinary (int(str(string[0])), 16)]
			else:
				if count == 1:
					self.opcode.append (pto)
				if count == 2:
					self.rs.append (pto)
			count = count + 1

		self.setCodeMachine ("".join(self.opcode))
		self.setCodeMachine ("".join(self.rs))
		self.setCodeMachine ("".join(self.rt))
		self.setCodeMachine ("".join(self.inof))

		return self.getCodeMachine ()

	# convertimos los tipo inmediato y offset
	def convertTiom (self):
		j = 0
		count = 1
		for pto in self.iset:
			if (pto == "rs" or pto == "base"):
				self.rs = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "rt":
				self.rt = [getRegFile_binary (self.code_assemb [j], self.reg_file)]
				j += 1
			elif pto == "inm" or pto == "off":
				self.inof = [literalToBinary (int(str(self.code_assemb [j])), 16)]
			else:
				if count == 1:
					self.opcode.append (pto)
				if count == 2:
					self.rs.append (pto)
			count = count + 1

		self.setCodeMachine ("".join(self.opcode))
		self.setCodeMachine ("".join(self.rs))
		self.setCodeMachine ("".join(self.rt))
		self.setCodeMachine ("".join(self.inof))

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
		if len(self.rs) != 0:
			self.rs.clear ()
		if len(self.rt) != 0:
			self.rt.clear ()
		if len(self.inof) != 0:
			self.inof.clear ()

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