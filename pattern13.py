a = int(input("Enter a no.: "))

for i in range(1,a+1,1):
    b=ord('A')
    for j in range(1,a+1,1):
        print(chr(b),end=" ")
        b+=1
    print()
