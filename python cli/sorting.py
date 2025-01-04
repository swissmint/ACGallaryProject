
def debuginsertionsort(unsortedlist):
    sortedlist = [0]
    i = 0
    index_minimum = 404
    counter = 0
    maximum = len(unsortedlist)
    while counter < maximum:
        minimum = 404
        for i in range(0, len(unsortedlist)):
            if unsortedlist[i] < minimum:
                print("old min: ", minimum)
                minimum = unsortedlist[i]
                print("new min: ", minimum)
                index_minimum = i
                print("yes", list_random[i])
            else:
                print("nope", list_random[i])
        print("old list: ", unsortedlist)
        unsortedlist.pop(index_minimum)
        print("new list: ", unsortedlist)
        sortedlist.append(minimum)
        print("sorted: ", sortedlist)
        counter += 1
    sortedlist.pop(0)
    return sortedlist

def insertionsort(unsortedlist):
    sortedlist = [0]
    i = 0
    index_minimum = 404
    counter = 0
    maximum = len(unsortedlist)
    while counter < maximum:
        minimum = 404
        for i in range(0, len(unsortedlist)):
            if unsortedlist[i] < minimum:
                minimum = unsortedlist[i]
                index_minimum = i
        unsortedlist.pop(index_minimum)
        sortedlist.append(minimum)
        counter += 1
    sortedlist.pop(0)
    return sortedlist


def datetoint(photo_list_f):
    try:
        return int(photo_list_f.replace(":", ""))
    except Exception:
        print("errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",photo_list_f)
        return int('0000:00:00:00:00:00'.replace(":", ""))

list_random = [1, 4, 9, 4, 5, 7, 3, 2, 5, 7, 4, 5, 3, 2, 4, 5, 4, 3, 3, 5, 5, 3, 2, 1]
new_list = [0]

listnon = [['2024:01:30:22:52:32', 'GIMP 2.10.36', '/home/noname/Pictures/phone pictures/BB8B02E5-7461-44A8-BAE9-20C0DB882C4D.jpg'], ['2023:05:18:18:10:50', 'iPhone 8', '16.4.1', '/home/noname/Pictures/phone pictures/IMG_1086.jpg'], ['2023:12:28:16:26:16', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1496.jpg'], ['2023:04:29:14:26:22', 'iPhone 8', '15.6.1', '/home/noname/Pictures/phone pictures/IMG_1047.jpg'], ['2023:12:26:13:42:04', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1439.jpg'], ['2023:12:26:13:44:15', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1447.jpg'], ['2023:12:26:13:49:58', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1453.jpg'], ['2023:12:26:13:29:29', 'iPhone 8', '16.7.2', '/home/noname/Pictures/phone pictures/IMG_1423.jpg']]
        

new_list = insertionsort(list_random)
print(new_list)


def debuginsertionsorttwo(unsortedlist):
    sortedlist = [0]
    i = 0
    index_minimum = 40400
    counter = 0

    maximum = len(unsortedlist)
    while counter < maximum:
        minimum = ["40400000000000000000000000"]
        for i in range(0, len(unsortedlist)):

            if datetoint(unsortedlist[i][0]) < datetoint(minimum[0]):
                print("old min: ", minimum)
                minimum = unsortedlist[i]
                print("new min: ", minimum)
                index_minimum = i
                print("yes", unsortedlist[i])
            else:
                print("nope", unsortedlist[i])
        print("old list: ", unsortedlist)
        unsortedlist.pop(index_minimum)
        print("new list: ", unsortedlist)
        sortedlist.append(minimum)
        print("sorted: ", sortedlist)
        counter += 1
    sortedlist.pop(0)
    return sortedlist

def insertionsorttwo(unsortedlist):
    sortedlist = [0]
    i = 0
    index_minimum = 40400
    counter = 0
    maximum = len(unsortedlist)
    while counter < maximum:
        minimum = ["4040000000000000000000"]
        for i in range(0, len(unsortedlist)):
            if datetoint(unsortedlist[i][0]) < datetoint(minimum[0]):
                minimum = unsortedlist[i]
                index_minimum = i
        unsortedlist.pop(index_minimum)
        sortedlist.append(minimum)
        counter += 1
    sortedlist.pop(0)
    return sortedlist
"""pui = debuginsertionsorttwo(listnon)
for i in pui:

    print(i[0])

min = 0
counter = 0
while counter > len(list):
    
    for e in range( list):

        if list[e] < min:
            min = list[e]
            list.pop(e)

    list.append(min)

    counter += 1



        # print(len(list_random)) # 24
        
    
                


"""



















