# 12) Write a python program to generate multiplication table.
def multiply_table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
    
multiply_table(float(input("Enter number to generate multiplication table: ")))

'''
Enter number to generate multiplication table: 3
3.0 X 1 = 3.0
3.0 X 2 = 6.0
3.0 X 3 = 9.0
3.0 X 4 = 12.0
3.0 X 5 = 15.0
3.0 X 6 = 18.0
3.0 X 7 = 21.0
3.0 X 8 = 24.0
3.0 X 9 = 27.0
3.0 X 10 = 30.0
'''