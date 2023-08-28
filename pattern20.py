a = int(input("Enter a no.: "))

for i in range(1,a+1,1):
    for j in range(a-i+1,1,-1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
