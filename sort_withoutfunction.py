mylist = [-25, 43, 54, 500, 400, 200, 600]
newlist = []
while mylist:
    max = mylist[0]
    for x in mylist:
        if x > max:
            max = x
    newlist.append(max)
    mylist.remove(max)

print(newlist)