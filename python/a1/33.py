# 33) Write a python program to display inverted half pyramid number pattern

def pyramid(rows):
    for i in range(rows, 0, -1):
        # print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
pyramid(rows)

'''
Enter the number of rows: 5
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''