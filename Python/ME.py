import pymcprotocol 
import AutoGui

PLC = pymcprotocol.Type3E() #Instanciando o FX5
PLC.setaccessopt(commtype="binary")
PLC.connect("192.168.100.22", 3456) #IP e porta

modelo_PCB = PLC.batchread_wordunits(headdevice="D16", readsize=1)
Modelo = int(str(modelo_PCB[0])[2:])

def ver_comm():
    print("ver comunicacao")

def troca_modelo():
    print("troca de modelo")

def ver_modelo():
    while True:
        Gcode_LA = PLC.batchread_wordunits(headdevice="D910", readsize=1)
        Gcode_LB = PLC.batchread_wordunits(headdevice="D930", readsize=1)

        print("ver modelo")
        if int(Gcode_LA[0]) != 0:
            valor_LA = int(chr((Gcode_LA[0] >> 8) & 0xFF) + chr((Gcode_LA[0] & 0xFF)))
            print("Confirma 1")
            AutoGui.confirme()
        if int(Gcode_LB[0]) != 0:
            valor_LB = int(chr((Gcode_LB[0] >> 8) & 0xFF) + chr((Gcode_LB[0] & 0xFF)))
            print("Confirma 2")
            AutoGui.confirme()

    ''''
    if valor_LA == Modelo and valor_LB == Modelo:
        ver_comm()
    else: troca_modelo()
    '''
def init():
    while True:
        modo_Maquina = PLC.batchread_wordunits(headdevice="D15", readsize=1)
        if int(modo_Maquina[0]) != 1:
            print("Aguardando:", modo_Maquina[0])
        elif int(modo_Maquina[0]) == 1:
            print("Inicializacao")
            ver_modelo()
            break
    return 0