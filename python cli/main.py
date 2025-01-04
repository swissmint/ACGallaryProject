# collect all photos - middle
# sort them - hard
# make an html page - sorta done
from sorting import insertionsorttwo, debuginsertionsorttwo
from Photos import photoreturn
from gallarymaker import makegallary


list_big = photoreturn("/home/noname/Pictures/phone pictures")
print("yup1")
list_big = debuginsertionsorttwo(list_big)
print("yup2")
makegallary(list_big, "/home/noname/Documents", "helloworld.html")
print("done!")