from typeI import TypeI
from functions import buildMatrix

codeMachine = []

type_i = TypeI ()

register_file 	= buildMatrix ("./codeV2/register-file.txt")
iset 	= ["lui","tim","010000","00000","rt","inm"]
assem 	= ["lui","$s1", "36"]

type_i.setISet(iset [2 : len(iset)])
type_i.setCodeAssembler (assem [1 : len(assem)])
type_i.setRegFile (register_file)

type_i.convert()

codeMachine = type_i.getCodeMachine ()

print (str(codeMachine))
