
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



list_random = [1, 4, 9, 4, 5, 7, 3, 2, 5, 7, 4, 5, 3, 2, 4, 5, 4, 3, 3, 5, 5, 3, 2, 1]
new_list = [0]


        

new_list = insertionsort(list_random)
print(new_list)



"""
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



















