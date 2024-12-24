list_random = [1, 4, 9, 4, 5, 7, 3, 2, 5, 7, 4, 5, 3, 2, 4, 5, 4, 3, 3, 5, 5, 3, 2, 1]
new_list = [0]
num  = len(new_list)
i = 0
maxmin = 13
minium = 10000
counter = 0
while not counter > len(list_random):
    print(len(list_random))
    
    for i in range(0, len(list_random)):
        if list_random[i] < minium:
            minium = list_random[i]
            maxmin = i
            
            print("yes", list_random[i])
        else:
            print("nope", list_random[i])
    
    print("------")
    list_random.pop(maxmin)
    print(minium)
    new_list.append(minium)

    counter += 1
new_list.pop(0) 
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






"""



















