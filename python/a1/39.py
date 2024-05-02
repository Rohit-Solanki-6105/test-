# 39) Write a python program to display pyramid pattern of alternate numbers

def alternate_number_pyramid(start, rows):
    num = start
    for i in range(1, rows + 1):
        print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 2
        print()

# Example usage
start_num = int(input("Enter the starting number: "))
rows = int(input("Enter the number of rows: "))
alternate_number_pyramid(start_num, rows)

'''
Enter the number of rows: 5
    1
   3 5
  7 9 11
 13 15 17 19
21 23 25 27 29
'''