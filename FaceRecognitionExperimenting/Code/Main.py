from VideoRecognition import VidRecognition
from GUI import InitializeTkinter

AccessMain = VidRecognition()


if AccessMain == True:
    print("access granted")
    InitializeTkinter()
else:
    print("acces denied")
