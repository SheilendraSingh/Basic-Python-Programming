"""
Output:-
Enter a no.: 5
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""

a = int(input("Enter a no.: "))

for i in range(a, 0, -1):
    for j in range(1, a + 1, 1):
        print(i, end=" ")
    print()
