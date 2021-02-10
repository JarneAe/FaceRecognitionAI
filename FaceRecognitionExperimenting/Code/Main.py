from VideoRecognition import VidRecognition
from LaunchGUI import InitializeTkinter

AccessMain = VidRecognition()
#AccessMain = True

if AccessMain == True:
    print("access granted")
    InitializeTkinter()
else:
    print("acces denied")
