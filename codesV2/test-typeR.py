from typeR import TypeR
from functions import buildMatrix

codeMachine = []

type_r = TypeR ()
register_file 	= buildMatrix ("register-file.txt")
iset 	= ["sll","tr","000000","00000","rd","rt","sa","000000"]
assem 	= ["sll","$s1", "$s2", "5"]

type_r.setISet(iset [2 : len(iset)])
type_r.setCodeAssembler (assem [1 : len(assem)])
type_r.setRegFile (register_file)

type_r.convert()

codeMachine = type_r.getCodeMachine ()

print (str(codeMachine))
