# 22) Write a python program to display prime numbers between two intervals.?
def prime_numbers(start, end):
    prime_numbers = []
    for possiblePrime in range(start, end + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            prime_numbers.append(possiblePrime)
    return prime_numbers

# Get user input for the interval
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Print the prime numbers in the interval
print("Prime numbers between {} and {} are:".format(start, end))
print(prime_numbers(start, end))

'''
Enter the starting range: 32
Enter the ending range: 56
Prime numbers between 32 and 56 are:
[37, 41, 43, 47, 53]
'''