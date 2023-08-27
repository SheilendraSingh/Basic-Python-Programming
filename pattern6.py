a = int(input("Enter a no.: "))
b=1
for i in range(a,0,-1):
    for j in range(1,a+1,1):
        print(b,end=" ")
        b+=1
    print()
