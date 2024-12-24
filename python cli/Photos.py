import os

path_to_photo = "/home/adminostrator/Pictures/AbigpictureFromIphone"
list_photo_path = []

dir_list = os.listdir(path_to_photo)      

for i in dir_list:
    fotos = os.scandir(path_to_photo + "/" + i)
    for e in fotos:
        if ".JPG" in e.name:
            list_photo_path.append(f"{i}/{e.name}")
            print(f"{i}/{e.name}")

    
print(list_photo_path)


