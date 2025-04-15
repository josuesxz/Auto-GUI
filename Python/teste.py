import pyautogui as robo
import pymcprotocol as PLC
import AutoGui

pymc3e = PLC.Type3E() #Instanciando o FX5
pymc3e.setaccessopt(commtype="binary")
pymc3e.connect("192.168.100.22", 3456) #IP e porta

modelo_PCB = pymc3e.batchread_wordunits(headdevice="D16", readsize=1)

robo.press("win") #acessando a barra de pesquisa do windows 
robo.write("cmd", interval=0.25) #acessando o cmd
robo.press("enter")
robo.press("space")
robo.write("Modelo da PCB = " + str(modelo_PCB[0]), interval=0.25)
#robo.rightClick(1143, 1050)
robo.PAUSE = 1.5
'''
robo.moveRel(0, -50, duration=0.5) #sobe alguns pixels para realizar o click
robo.click()
'''
AutoGui.close_window()