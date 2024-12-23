
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
    list = list_that_contians_the_date.replace(" ", ":")
    list = list.split(":")
    return list

def makelist(list):
    for i in range(1, len(list)):
        j = i
        while list[j - 1] > list[j] and j > 0:
            list[j - 1], list[j] = list[j], list[j - 1]
            j -= 1
    return list

def makelisttwo(list):
    for i in range(1, len(list)):
        j = i[1]
        j = makedate(j)
        while list[j - 1] > list[j] and j > 0:
            list[j - 1], list[j] = list[j], list[j - 1]
            j -= 1
    return list  

list_three = ['2024:04:01 18:06:01', '2024:03:23 11:26:53', "",'2024:03:30 15:15:06']
list_two = [
['IMG_1616.jpg', '2024:04:01 18:06:01', 'iPhone 8', '16.7.4'], 
['IMG_1608.jpg', '2024:03:23 11:26:53', 'iPhone 8', '16.7.4'], 
['TF.jpeg'], 
['IMG_1612.jpg', '2024:03:30 15:15:06', 'iPhone 8', '16.7.4']] 
list = [ 1, 4, 9, 5, 2, 7, 6, 2, 8, ]
print(makelist(list))

for i in range(0, len(list_three)):
    list_three[i] = makedate(list_three[i])
print(list_three)

print(compareList(list_three[1][], list_three[2][] ))
