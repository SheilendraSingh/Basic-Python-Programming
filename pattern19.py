a = int(input("Enter a no.: "))

for i in range(1,a+1,1):
    b=ord('A')+a-i
    for j in range(1,i+1,1):
        print(chr(b),end=" ")
        b+=1
    print()
