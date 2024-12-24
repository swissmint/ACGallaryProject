import os
from PIL import Image
from PIL.ExifTags import TAGS

liststuff = []
foto_names = []
foto_date_type_version = []
new_foto_date_type_version = []

first_half_html = """<!DOCTYPE html>
<html>

    <head>
		<link rel="icon" href="">
		<link rel="stylesheet" href="app.css">
		<link rel="stylesheet" href="lightbox.css">
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
        <title>Gallery</title>
    </head>

    <body style="font-family:Verdana;color:#ffffff;">
        
        <div class="container">
            <div class="heading">
                <h3>Photo Gallery version 1</h3>
            </div>
            <div class="box">
           """
secound_half_html = """
                
            </div>
        </div>
        <script src="lightbox-plus-jquery.min.js"></script>
       
    </body>

</html>"""

def compareList(datelist, secound_datelist):
    datelist.reverse()
    secound_datelist.reverse()
    n = 0
    for i in range(0, len(datelist)):
        if int(datelist[i]) < int(secound_datelist[i]):
            return 0
        if int(datelist[i]) > int(secound_datelist[i]):
            return 1
        if n == 5:
                return 0

def makedate(list_that_contians_the_date):
    list = list_that_contians_the_date[1].replace(" ", ":")
    list = list.split(":")
    return list

def sumlist(list_one, list_two):
    for i in list_two:
        list_one.append(i)
    print("done")
    return list_one

def makeblock(list, path_to_photo):
    block_list = ""
    for i in (list):
        if i.find(".AAE") != -1:
            continue
        block_list = block_list + f"""
                    <div class="zoom-in">
                        <a href="{path_to_photo}{i}" data-lightbox="models" data-title="Caption1">
                            <img src="{path_to_photo}{i}" alt="">
                        </a>
                    </div>\n"""
    return block_list

def savegallery(path, title, text):
    with open(path, 'w') as fp:
        print("saving gallery...", title)
        fp.write(text)
        # print(text)
        fp.close()
    print("finish saving ", title)

def takeallphotosShort(dir):
    for i in os.listdir(dir): #/home/adminostrator/Documents/JustI.T.stuff/GallaryProject/python cli/uploads"):
        foto_names.append(i)

    print(foto_names, "\n")

    return foto_names

def takeallphotos(dir):
    for i in os.listdir(dir): #/home/adminostrator/Documents/JustI.T.stuff/GallaryProject/python cli/uploads"):
        foto_names.append(i)
    exif = {}

    for i in range(0, len(foto_names)):

        image = Image.open(dir + foto_names[i])

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
        exif = {}
        foto_date_type_version.append(liststuff)
        liststuff = []
            
    print(foto_names)
    print(foto_date_type_version)

    for i in range(0, len(foto_names)):
        foto_date_type_version[i].insert(0, foto_names[i]) 

    print(foto_date_type_version, "\n")

    return foto_date_type_version




"""if len(new_foto_date_type_version) == 0:
    new_foto_date_type_version = [foto_date_type_version[0]]
    print(new_foto_date_type_version)"""

foto_date_type_version = takeallphotosShort("/home/adminostrator/Pictures/jbig picture/allfoto/")# make giagentic list

block_list = makeblock(foto_date_type_version, "/home/adminostrator/Pictures/jbig picture/allfoto/")
"""

foto_date_type_version = foto_date_type_version.append(takeallphotosShort("/home/adminostrator/Pictures/jbig picture/202406__"))
foto_date_type_version = foto_date_type_version.append(takeallphotosShort("/home/adminostrator/Pictures/jbig picture/202405__"))"""


finaltext = first_half_html + "\n" + block_list + "\n" + secound_half_html

print(finaltext)

savegallery("/home/adminostrator/Documents/JustI.T.stuff/GallaryProject/gallery/index.html", "index.html", finaltext)

"""

hello.txt 

if hello.txt.find(".aee")
continue

i = 0
for i in range(0, len(foto_date_type_version)):

    old_string_list = foto_date_type_version[i]
    print(": ", old_string_list,"\n", foto_date_type_version ,"\n",i)

    if len(old_string_list) < 2:
        continue

    for d in range(0, len(new_foto_date_type_version)):        

        new_string_list_date = new_foto_date_type_version[d]

        print(": new", d ,"\n", new_string_list_date,"\n", new_foto_date_type_version)
        try:
            new_string_list_date_future = new_foto_date_type_version[d - 1]
        except IndexError:
            print("list to short")
"""
        # stores dates
"""
        string_date = makedate(old_string_list)

        new_string_date = makedate(new_string_list_date)

        new_string_date_future = makedate(new_string_list_date_future)
        try:
            string_date_future = makedate(old_string_list_future)
        except IndexError:
            string_date_future = [0, 0, 0, 0, 0, 0, 0]
            print("list to short")

        print("o : ", string_date)
        print("n : ", new_string_date)

        choise = compareList(new_string_date, string_date)

        future_choise = compareList(new_string_date_future, string_date_future)

        if choise == 0:
            new_foto_date_type_version.insert(d - 1, foto_date_type_version[i])

        if choise == 1:
            if future_choise == 1:
                continue
            new_foto_date_type_version.insert(d, foto_date_type_version[i])


for i in range(0, len(new_foto_date_type_version)):

    print(": ", new_foto_date_type_version[i][1])


"""
"""
new_dictionary = {}
new_dictionary = list(foto_stuff_dictionary.keys())
print(new_dictionary, "hello world")

if len(new_dictionary) == 1:
    for i in range(0, len(foto_stuff_dictionary)):
        print(i)
        
        new_date_string = new_dictionary[i][1] 
        old_date_string = foto_stuff_dictionary[i][1]
        print(new_date_string)
        print(old_date_string)
        
        for i in len(list):
            if list[i] > number:
                list.insert(i - 1, new_date_string)
                
for i in list

    check 0 seclist add i continue

    stredatelist = i.strdate

    for d in seclist:

        choise = comparelist(d[+1],f dasfj)
        choisefutre = comparelist(d[+2] srtad)

        if choise == 0
            ifchoisefrut== 0:
                continue
            d.insert()

            d.iners
        if choise == 1
            if choisefutre == 1:
                continue
            d.insert()

add those who have no date
            

list = [ "23313" ,"21", "12", "01"]
listtwo = [ "23313" ,"22", "12", "01"]
        


print(compareList(list, listtwo))



- get the names of the fotos :)
- get the dates of the fotos :)
- par thems up :)

if year



"""
