
# 37) Write a python program to display even number pyramid pattern

def even_number_pyramid(rows):
    num = 2
    for i in range(1, rows + 1):
        print(" "*(rows-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 2
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
even_number_pyramid(rows)

'''
Enter the number of rows: 5
    2
   4 6
  8 10 12
 14 16 18 20
22 24 26 28 30
'''