word=input("Enter the word:")
l=len(word)
for x in word[0:l]:
    if x==word[0]:
        print("$",end="")
    elif word[0]==word[0]:
        print(x,end="")
    else:
        print(x)