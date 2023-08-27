"""
Output:-
Enter a no.: 5
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

a = int(input("Enter a no.: "))
b = 1
for i in range(1, a + 1, 1):
    for j in range(1, i + 1, 1):
        print(b, end=" ")
        b += 1
    print()
