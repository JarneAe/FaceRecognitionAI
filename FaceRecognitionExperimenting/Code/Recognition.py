from PIL import Image, ImageDraw, ImageFont
import face_recognition


pil_image = ''
name = ''

def Recognition():
    global name
    global pil_image
    obama_image = face_recognition.load_image_file("Images\Obama.jpg")
    obama_face_encodings = face_recognition.face_encodings(obama_image) [0]

    robertdowney_image = face_recognition.load_image_file("Images\\robertdowney.jpg")
    robertdowney_face_encodings = face_recognition.face_encodings(robertdowney_image) [0]

    favreau_image = face_recognition.load_image_file("Images\\favreau.jpg")
    favreau_face_encodings = face_recognition.face_encodings(favreau_image) [0]

    Mickey_image = face_recognition.load_image_file("Images\Mickey.jpg")
    Mickey_face_encodings = face_recognition.face_encodings(Mickey_image) [0]

    Scarlett_image = face_recognition.load_image_file("Images\Scarlett.jpg")
    Scarlett_face_encodings = face_recognition.face_encodings(Scarlett_image) [0]

    Gwyneth_image = face_recognition.load_image_file("Images\Gwyneth.jpg")
    Gwyneth_face_encodings = face_recognition.face_encodings(Gwyneth_image) [0]

    Don_image = face_recognition.load_image_file("Images\Don.jpg")
    Don_face_encodings = face_recognition.face_encodings(Don_image) [0]

    known_face_encodings = [
        obama_face_encodings,
        robertdowney_face_encodings,
        favreau_face_encodings,
        Mickey_face_encodings,
        Scarlett_face_encodings,
        Gwyneth_face_encodings,
        Don_face_encodings

    ]


    known_face_names = [
        "Obama",
        "Robert Downey Jr.",
        "Jon Favreau",
        "Mickey Rourke",
        "Scarlett Johansson",
        "Gwyneth Paltrow",
        "Don Cheadle"
    ]



    image = face_recognition.load_image_file("Images\ironmancast.jpg")

    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)


    pil_image = Image.fromarray(image)
    draw = ImageDraw.Draw(pil_image)

    for(top,right,bottom,left), face_encodings in zip(face_locations,face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings)

        name = "Unidentified User"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        draw.rectangle(((left,top),(right,bottom)),outline=(0,0,255),width=(2))
        font = ImageFont.truetype("Fonts\LEMONMILK-Regular.otf",12)
        text_width,text_height = draw.textsize(name)
        draw.rectangle(((left,bottom - text_height - 10),(right,bottom)), fill=(0,0,255),outline=(0,0,255))
        draw.text((left + 6, bottom - text_height -5),name,font=font, fill=(255,255,255,255))

    
    del draw




Recognition()

