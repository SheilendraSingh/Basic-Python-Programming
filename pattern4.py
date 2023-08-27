"""
Output:-
Enter a no.: 5
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""

a = int(input("Enter a no.: "))

for i in range(a, 0, -1):
    for j in range(a, 0, -1):
        print(j, end=" ")
    print()
