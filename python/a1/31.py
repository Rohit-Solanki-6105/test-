# 31) Write a python program to display inverted pyramid of the same digit
def pyramid(num, rows):
    for i in range(rows, 0, -1):
        print(" "*(rows-i),str(num)*(2*i-1))
pyramid(int(input("Number: ")), int(input("Rows: ")))

'''
Number: 5
Rows: 6
 55555555555
  555555555
   5555555
    55555
     555
      5
      '''