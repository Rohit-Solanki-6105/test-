# 40) Write a python program to display mirrored pyramid (right-angled triangle) pattern of numbers

def mirrored_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        for j in range(i, 0, -1):
            print(j, end='')
        for k in range(2, i + 1):
            print(k, end='')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
mirrored_pyramid(rows)

'''
Enter the number of rows: 5
    1
   212
  32123
 4321234
543212345
'''
