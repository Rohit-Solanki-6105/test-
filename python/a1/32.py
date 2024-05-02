# 32) Write a python program to display reverse pyramid of numbers
def reverse_pyramid_numbers(rows):
    num = 1
    for i in range(rows, 0, -1):
        print(' '*(rows - i), end='')
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
reverse_pyramid_numbers(rows)

'''
Enter the number of rows: 6
1 2 3 4 5 6
 7 8 9 10 11
  12 13 14 15
   16 17 18
    19 20
     21
     '''
