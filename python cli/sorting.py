list_random = [1, 4, 9, 4, 5, 7, 3, 2, 5, 7, 4, 5, 3, 2, 4, 5, 4, 3, 3, 5, 5, 3, 2, 1]
new_list = [0]
num  = len(new_list)
i = 0
index_minimum = 404
minimum = 404
counter = 0
maximum = len(list_random)
while counter < maximum:

    print(len(list_random)) # 24
    
    for i in range(0, len(list_random)):
        if list_random[i] < minimum:
            print("old min: ", minimum)
            minimum = list_random[i]
            print("new min: ", minimum)
            index_minimum = i
            
            print("yes", list_random[i])
        else:
            print("nope", list_random[i])
    
    
    print(list_random)
    list_random.pop(index_minimum)
    print(list_random)
    new_list.append(minimum)
    print("newww: ", new_list)
    counter += 1
    print("he: ", counter)
    minimum = 404
    print("------")


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



















