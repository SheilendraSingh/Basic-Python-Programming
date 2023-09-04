a = int(input("Enter a no.: "))
b=1
for i in range(1,a+1,1):
    for j in range(0,a-i,1):
        print(" ",end=" ")
    for j in range(1,i+1,1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
