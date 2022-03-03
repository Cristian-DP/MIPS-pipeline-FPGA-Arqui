from functions import buildMatrix

register_file 	= buildMatrix ("register-file.txt")
instruction_set	= buildMatrix ("read-instruction-set.txt")
code			= buildMatrix ("assembler.txt")
ass 			= buildMatrix ("assembler-code.asm")

#print (register_file)
#print (instruction_set)
#print (code)
print (ass)