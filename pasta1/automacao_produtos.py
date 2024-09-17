import pyautogui as py
import pandas as pd
import time

py.PAUSE=2
py.click(310,718,duration=2)
py.hotkey('command','t')
py.typewrite('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')
time.sleep(3)
py.press('tab')
py.typewrite('samgarcia@gmail')
py.press('tab')
py.typewrite('Senha')
py.press('tab')
py.press('enter')
time.sleep(2)

for line in arquivo.index:
    codigo=str((arquivo.loc[line, 'codigo']))
    py.click(x=891, y=283)
    py.write(codigo)
    py.press('tab')
    py.write(arquivo.loc[line, 'marca'])
    py.press('tab')
    py.write(arquivo.loc[line, 'tipo'])
    py.press('tab')
    py.write(str(arquivo.loc[line, 'categoria']))
    py.press('tab')
    py.write(str(arquivo.loc[line, 'preco_unitario']))
    py.press('tab')
    py.write(str(arquivo.loc[line, 'custo']))
    py.press('tab')
    obs = str(arquivo.loc[line, 'obs'])
    if obs != "nan":
        py.write('aaa')
    py.press('tab')
    py.press('enter')
    py.scroll(5000)
