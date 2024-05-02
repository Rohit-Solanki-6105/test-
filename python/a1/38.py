# 38) Write a python program to display pyramid of horizontal tables

def horizontal_table_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i),end="")
        for j in range(1, i + 1):
            print(f"{i*j:4}", end=' ')
        print()

# Example usage
rows = int(input("Enter the number of rows: "))
horizontal_table_pyramid(rows)

'''
Enter the number of rows: 5
       1
      2    4
     3    6    9
    4    8   12   16
   5   10   15   20   25
'''
