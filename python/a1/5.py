# 5) Write a python program to check whether number is even or odd.
def check_even(num):
    if num%2 == 0: 
        print("Even")
        # return True
    print("Odd")
    # return False
check_even(int(input("Enter int: ")))
# print(check_even(int(input("Enter number: "))))

'''
Enter int: 3
Odd

Enter int: 4
Even
'''