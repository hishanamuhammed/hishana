L1=[10,20,30,40,50]
L2=[50,60,70]
print(len(L1))
print(len(L2))
total1=sum(L1)
print("Sum of L1:",total1)
total2=sum(L2)
print("Sum of L2:",total2)
L3=[]
for n in L1:
  if n in L2:
    if n not in L3:
      L3.append(n)
print(L3)