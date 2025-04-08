# collect all photos - middle
# sort them - hard
# make an html page - sorta done
from sorting import insertionsorttwo, debuginsertionsorttwo
from Photos import photoreturn
from gallarymaker import makegallary

print("beginn")
list_big = photoreturn("/run/user/1000/gvfs/gphoto2:host=Apple_Inc._iPhone_00008101000A215E22C3001E/202502__") # "/run/user/1000/gvfs/gphoto2:host=Apple_Inc._iPhone_00008101000A215E22C3001E")
print("yup1")
list_big = insertionsorttwo(list_big)
print("yup2")
makegallary(list_big, "/home/adminostrator/Documents/AApythonProjects/ACGallaryProject/mess/gallery/index.html", "index.html")
print("done!")