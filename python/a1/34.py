# 34) Write a python program to display pyramid of natural numbers less than 10

def pyramid_natural_numbers():
    num = 1
    for i in range(1, 5):
        print(" "*(5-i), end="")
        for j in range(1, i + 1):
            print(num, end=' ')
            num += 1
        print()

# Example usage
pyramid_natural_numbers()

'''
    1 
   2 3
  4 5 6
 7 8 9 10
'''
