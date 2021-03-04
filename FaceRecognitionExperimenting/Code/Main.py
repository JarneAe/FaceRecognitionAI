from VideoRecognition import VidRecognition,name
from LaunchGUI import InitializeTkinter

VidRecognition()


if name == "Jarne":
    print("access granted")
    InitializeTkinter()
else:
    print("acces denied")
