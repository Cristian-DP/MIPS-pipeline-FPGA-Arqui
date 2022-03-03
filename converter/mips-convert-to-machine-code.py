import re

writeMachineCode = open('machine-code.txt', 'r+')
writeMachineCode.truncate(0)

readInstructionSet = open( 'read-instruction-set.txt', 'r')
instructionSet = readInstructionSet.readlines()

readRegisters = open( 'read-registers.txt', 'r')
registersSet = readRegisters.readlines()

readAssembler = open( 'assembler.asm', 'r' )
asemblerCode = readAssembler.readlines()

for assemblerInstruction in asemblerCode:
    
    assemblerInstruction = assemblerInstruction.replace(',', ' ').split()
    newMachineCodeLine = ''
    
    registroUno = ""
    registroDos = ""
    registroTres = ""
    literal = ""
    
    for instructionSetLine in instructionSet:

        instructionSetLineSplit = instructionSetLine.split()

        if( assemblerInstruction[0] == instructionSetLineSplit[0] ):

            writeMachineCode.write( instructionSetLineSplit[1] + ' ')
            
            # instruccion de TIPO R
            if( instructionSetLineSplit[2] == 'r' ):
                isMatch = re.search(".+\$(?:t|s)(?:.+), \$(?:t|s)(?:.+), \$(?:t|s)(?:.+)", instructionSetLine)
                # Si encuentra un match se trata de una instruccion de tipo R SIN shift
                if isMatch:
                    print("estoy aca")
                    for registersSetLine in registersSet:
                        registersSetLineSplit = registersSetLine.split()
                        if ( registroUno == "" and assemblerInstruction[1] == registersSetLineSplit[0] ):
                            registroUno = format( int(registersSetLineSplit[1]), '05b')
                        if ( registroDos == "" and assemblerInstruction[2] == registersSetLineSplit[0] ):
                            registroDos = format( int(registersSetLineSplit[1]), '05b')
                        if ( registroTres == "" and assemblerInstruction[3] == registersSetLineSplit[0] ):
                            registroTres = format( int(registersSetLineSplit[1]), '05b')

                    writeMachineCode.write( registroUno +' '+ registroDos +' ' \
                    + registroTres + ' 00000 ' + instructionSetLineSplit[3] + '\n')
                # De lo contrario es una instruccion de tipo R con operacion Shift   
                else:
                    for registersSetLine in registersSet:
                        registersSetLineSplit = registersSetLine.split()
                        if ( registroUno == "" and assemblerInstruction[1] == registersSetLineSplit[0] ):
                            registroUno = format( int(registersSetLineSplit[1]), '05b')
                        if ( registroDos == "" and assemblerInstruction[2] == registersSetLineSplit[0] ):
                            registroDos = format( int(registersSetLineSplit[1]), '05b')
                    literal = format( int(assemblerInstruction[3]), '05b')

                    writeMachineCode.write( registroUno +' '+ registroDos +' ' \
                    + literal + ' ' + instructionSetLineSplit[3] + '\n')
            
            # instruccion de TIPO I
            elif( instructionSetLineSplit[2] == 'i' ):
                print(assemblerInstruction)
                writeMachineCode.write( assemblerInstruction[1] +' '+ assemblerInstruction[2] )
                writeMachineCode.write( '\n' )
            
            # instruccion de TIPO J
            elif( instructionSetLineSplit[2] == 'j' ):
                writeMachineCode.write( assemblerInstruction[1] )
                writeMachineCode.write( '\n' )
