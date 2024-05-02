
# 36) Write a python program to display connected inverted pyramid pattern of numbers

def connected_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print(j, end='')
        for k in range(i, 0, -1):
            print(k, end='')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
connected_inverted_pyramid(rows)

'''
Enter the number of rows: 5
1234554321
 12344321
  123321
   1221
    11
    '''
