"""
Output:-
Enter a no.: 5
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
"""


a = int(input("Enter a no.: "))
b = 1
for i in range(1, a + 1, 1):
    for j in range(i, (i * 2), 1):
        print(j, end=" ")
        b += 1
    print()
