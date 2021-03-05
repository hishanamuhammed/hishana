#List Comprehensions

list=[3,6,-2,0,-6,-2,5,1,9]
newlist=[x for x in list if x>0]
print(newlist)


N=int(input("Enter number of no: "))
list=[]
for x in range(N):
  x=int(input("Enter no: "))
  list.append(x)
print(list)
squarelist=[x**2 for x in list]
print(squarelist)


word="umberella"
vowels="aeiou"
list=[x for x in word if x in vowels]
print(list)


word="flower"
list=[ord(x) for x in word]
print(list)