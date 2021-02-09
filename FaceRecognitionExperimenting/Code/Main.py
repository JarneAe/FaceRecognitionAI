from Recognition import Recognition
from Recognition import name
from Recognition import pil_image
from GUI import InitializeTkinter


if name == "Obama":
    print("access granted")
    InitializeTkinter()
else:
    print("acces denied")

pil_image.show()