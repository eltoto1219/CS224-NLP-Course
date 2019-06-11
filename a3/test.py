import copy 

l1 = [1,2,["fuck", "you"],3,4,5,]

l2 = copy.copy(l1)

print(l1)

l2[2].pop()
l1.append("fuck")
print(len(l1))

for i in range(0, len(l1)):
    print(i)

print(l1)

