import os
from PIL import Image
from PIL.ExifTags import TAGS

def takeallphotos(path, photo_list):
    complete_photo_list = []
    liststuff = []
    exif = {}

    for i in range(0, len(photo_list)):

        try:
            image = Image.open(photo_list[i])
        except OSError:
            print("not good1")
            # add os creation date
            complete_photo_list.append(['0000:00:00:00:00:00', photo_list[i]])
            continue
        for tag, value in image.getexif().items():
            if tag in TAGS:
                exif[TAGS[tag]] = value
                # print(TAGS[tag], tag ,value)

        if "DateTime" in exif:
            liststuff.append(exif["DateTime"].replace(" ", ":"))
        if "HostComputer" in exif:
            liststuff.append(exif["HostComputer"])
        if "Software" in exif:
            liststuff.append(exif["Software"])
        liststuff.append(photo_list[i])
        exif = {}
        complete_photo_list.append(liststuff)
        liststuff = []

    # print(complete_photo_list)

    return complete_photo_list

path_to_photo = "/home/noname/Pictures/phone pictures"

def photoreturn(path_to_photo):
    list_photo_path = []
    dir_list = os.listdir(path_to_photo)      

    if ".jpg" in dir_list[0]:
        for i in dir_list:
            if ".jpg" in i: 
                list_photo_path.append(f"{path_to_photo}/{i}")
    else:
        for i in dir_list:
            fotos = os.scandir(path_to_photo + "/" + i)
            for e in fotos:
                if ".JPG" in e.name:
                    list_photo_path.append(f"{path_to_photo}/{i}/{e.name}")
                    print(f"{path_to_photo}/{i}/{e.name}")
                

    
    return takeallphotos(path_to_photo, list_photo_path)



#  night core