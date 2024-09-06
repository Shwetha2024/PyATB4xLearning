# shopping list



mylist=["chair", "table","sofa","stool"]
print(len(mylist))

def furniture(a):
    b=input("Enter the item to be added\n")
    #a.append(b)
    #a.append("plantpot")
    #print(len(a))
    a.insert(2,b)
    a.remove("chair")
    return a


test=furniture(mylist)
print(test)
print(len(test))
