
#list

my_list=["bread","butter","cheese"]
print(my_list)
print(len(my_list))

my_list[1]="Mr"
print(my_list)

#print(my_list[10])

for i in my_list:
    print(i)

my_list.append("patty")
my_list.append("sauce")
print(my_list)

my_list.extend(["tomato","onion","lettuce"])
print(my_list)
my_list.extend(["cucumber"])
print(my_list)

my_list.insert(6,"pepper")
print(my_list)
my_list.insert(-2,"salt")
print(my_list)
my_list.remove("Mr")
print(my_list)

my_list2=my_list.copy()
print(my_list2)

my_list2.reverse()
print(my_list2)

my_list1=[2,8,4,6]
print(my_list1)
my_list1.reverse()
print(my_list1)
my_list1.sort(reverse=True )
print(my_list1)
my_list1.sort()
print(my_list1)

list3=[9,8,7,6]
print(list3)
list3.pop()
print(list3)