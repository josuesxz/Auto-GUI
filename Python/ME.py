import pymcprotocol 
import AutoGui

PLC = pymcprotocol.Type3E() #Instanciando o FX5
PLC.setaccessopt(commtype="binary")
PLC.connect("192.168.100.22", 3456) #IP e porta

modelo_PCB = PLC.batchread_wordunits(headdevice="D16", readsize=1)
modo_Maquina = PLC.batchread_wordunits(headdevice="D0", readsize=1)
Gcode_LA = PLC.batchread_wordunits(headdevice="D910", readsize=1)
Gcode_LB = PLC.batchread_wordunits(headdevice="D930", readsize=1)

valor_LA = chr((Gcode_LB[0] >> 8) & 0xFF) + chr((Gcode_LB[0] & 0xFF))
valor_LB = chr((Gcode_LA[0] >> 8) & 0xFF) + chr((Gcode_LA[0] & 0xFF))
Modelo = str(modelo_PCB[0])[2:]

def ver_modelo():
    print("ver modelo")
    if int(valor_LA) != 0:
        print("Confirma 1")
        AutoGui.confirme
    elif int(valor_LB) != 0:
        AutoGui.confirme
        print("Confirma 2")

def init():
    while True:
        if modo_Maquina[0] == 8:
            print("Inicializacao")
            ver_modelo()
        else: print("Aguardando")
    return 0

print(int(valor_LB))