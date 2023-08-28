a = int(input("Enter a no.: "))
b=1
for i in range(1,a+1,1):
    for j in range(i,0,-1):
        print(j,end=" ")
        b+=1
    print()
