# 41) Write a python program to display equilateral triangle with stars (asterisk symbol)

def equilateral_triangle_boundary(rows):
    for i in range(rows):
        if i == 0:
            print(' ' * (rows - 1) + '*')
        elif i == rows - 1:
            print(' ' * (rows - i - 1) + '* ' * (i + 1))
        else:
            print(' ' * (rows - i - 1) + '*' + ' ' * (2 * i - 1) + '*')


def equilateral_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)


# Input number of rows
rows = int(input("Enter the number of rows: "))


equilateral_triangle_boundary(rows)
equilateral_triangle(rows)

'''
Enter the number of rows: 5
    *
   * *
  *   *
 *     *
* * * * *
    *
   * *
  * * *
 * * * *
* * * * *
'''