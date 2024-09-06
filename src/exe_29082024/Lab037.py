set1={"check1","3","check2","check3"}
print(len(set1))
print(set1)

for e in set1:
    print(e)


set1.add("check4")
print(set1)
set1.add("check4")
print(set1)

set={"check6","check4","3"}
set2=set1.union(set)
print(set2)

set3=set2
print(set3)