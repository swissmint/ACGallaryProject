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

def makeblock(list_of_stuff):
    counter = 0
    block_list = ""
    for i in (list_of_stuff):
        print()
        path = list_of_stuff[counter][2]
        
        block_list = block_list + f"""
                    <div class="zoom-in">
                        <a href="{path}" data-lightbox="models" data-title="Caption1">
                            <img src="{path}" alt="">
                        </a>
                    </div>\n"""
        counter += 1
    return block_list

listnon = [['2024:01:30:22:52:32', 'GIMP 2.10.36', '/home/noname/Pictures/phone pictures/BB8B02E5-7461-44A8-BAE9-20C0DB882C4D.jpg'], ['2023:05:18:18:10:50', 'iPhone 8', '16.4.1', '/home/noname/Pictures/phone pictures/IMG_1086.jpg'], ['2023:12:28:16:26:16', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1496.jpg'], ['2023:04:29:14:26:22', 'iPhone 8', '15.6.1', '/home/noname/Pictures/phone pictures/IMG_1047.jpg'], ['2023:12:26:13:42:04', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1439.jpg'], ['2023:12:26:13:44:15', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1447.jpg'], ['2023:12:26:13:49:58', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1453.jpg'], ['2023:12:26:13:29:29', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1423.jpg']]
print(makeblock(listnon))

def savegallery(path, title, text):
    with open(path, 'w') as fp:
        print("saving gallery...", title)
        fp.write(text)
        # print(text)
        fp.close()
    print("finish saving ", title)



def makegallary(list_of_stuff, path_to_save_gallary, title):
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
    block_middle = makeblock(list_of_stuff)
    full_block = first_half_html + block_middle + secound_half_html
    savegallery(path_to_save_gallary, title, full_block)
    print("done!")

 