a = int(input("Enter a no.: "))

for i in range(1,a+1,1):
    for j in range(0,a-i,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print(i,end=" ")
    print()
