a = int(input("Enter a no.: "))
b=1
for i in range(1,a+1,1):
    for j in range(0,a-i,1):
        print(" ",end=" ")
    for j in range(0,i,1):
        print(b,end=" ")
        b+=1
    print()
