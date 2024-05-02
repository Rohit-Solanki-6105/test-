# 24) Write a python program to display armstrong number between two intervals.?
# Function to find Armstrong numbers in a given interval
def find_Armstrong(lower, upper):
    # Iterate over numbers from lower to upper
    for num in range(lower, upper+1):
        # Calculate the sum of the cubes of the digits
        sum = 0
        temp = num
        order = len(str(num))
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
        # Check if the number is an Armstrong number
        if num == sum:
            print(num)

# Replace these values with the desired interval
lower = 100
upper = 2000

# Call the function to find Armstrong numbers
find_Armstrong(lower, upper)

'''
153
370
371
407
1634
'''