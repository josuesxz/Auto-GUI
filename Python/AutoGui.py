import pyautogui as robo

def close_window():
    with robo.hold('alt'):
        robo.press('f4')

def confirme():
    robo.press("win")