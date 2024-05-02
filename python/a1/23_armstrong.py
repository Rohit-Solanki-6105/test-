# 23) Write a python program to check armstrong number.
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

lenth_num = len(str(num))
print(lenth_num)

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += (digit ** lenth_num)
   print(digit, "^", lenth_num, "+= sum = ", sum)
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

'''
Enter a number: 153
153 is an Armstrong number
'''
# 1, 1296, 81, 1694, 256
