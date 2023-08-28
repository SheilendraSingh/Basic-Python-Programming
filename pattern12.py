a = int(input("Enter a no.: "))
b=ord('A')
for i in range(1,a+1,1):
    for j in range(1,a+1,1):
        print(chr(b),end=" ")
    b+=1
    print()
