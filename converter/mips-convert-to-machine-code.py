writeMachineCode = open('machine-code.txt', 'r+')
writeMachineCode.truncate(0)

readInstructionSet = open( 'read-instruction-set.txt', 'r')
instructionSet = readInstructionSet.readlines()

readAssembler = open( 'assembler.txt', 'r' )
asemblerCode = readAssembler.readlines()

for assemblerInstruction in asemblerCode:
    
    assemblerInstruction = assemblerInstruction.replace(',', ' ').split()
    newMachineCodeLine = ''
    
    for instructionSetLine in instructionSet:

        instructionSetLine = instructionSetLine.split()

        if( assemblerInstruction[0] == instructionSetLine[0] ):

            writeMachineCode.write( instructionSetLine[1] + ' ')
            
            if( instructionSetLine[2] == 'r' ):
                writeMachineCode.write( assemblerInstruction[1] +' '+ assemblerInstruction[2] +' ' \
                + assemblerInstruction[3] + ' 00000 ' + instructionSetLine[3] )
                writeMachineCode.write( '\n' )
            
            elif( instructionSetLine[2] == 'i' ):
                print(assemblerInstruction)
                writeMachineCode.write( assemblerInstruction[1] +' '+ assemblerInstruction[2] )
                writeMachineCode.write( '\n' )
                
            elif( instructionSetLine[2] == 'j' ):
                writeMachineCode.write( assemblerInstruction[1] )
                writeMachineCode.write( '\n' )
