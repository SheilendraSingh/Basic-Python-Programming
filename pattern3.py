"""
Output:-
Enter a no.: 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

a = int(input("Enter a no.: "))

for i in range(1, a + 1, 1):
    for j in range(1, a + 1, 1):
        print(j, end=" ")
    print()
