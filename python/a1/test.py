# def pyramid(num):
#     for i in range(0,num):
#         # print(i, end=" = ")
#         print("*"*(num-i), " "*(2*i), "*"*(num-i))
#         # print(f"i: {i},  num - i: {num - i}, 2*i : {2*i}")
    
#     # print("----------------------------")
#     for i in range(num, -1, -1):
#         # print(i, end=" = ")
#         print("*"*(num-i), " "*(2*i), "*"*(num-i))

# pyramid(10)

# def pyramid(num):
#     for i in range(num):
#         print(" "*(num-i), "*"*(2*i-1))

#     for i in range(num, -1, -1):
#         print(" "*(num-i), "*"*(2*i-1))

# def pyramid(num):
#     for i in range(num, 0, -1):
#         print('*'*(i), " ", "*"*(num-i), end="")
#         print("*"*(num-i), " ", "*"*(i))

#     for i in range(num+1):
#         print('*'*(i), " ", "*"*(num-i), end="")
#         print("*"*(num-i), " ", "*"*(i))

# def pyramid(num):
#     for i in range(num):
#         print(" "*(num-i),  "*"*(2*i+1))

#     for i in range(3):
#         print(" "*(num),  "*")

# def pyramid(num):


# pyramid(10)

# def calc(n1, op, n2):
#     match(op):
#         case  "+": return n1 + n2
#         case "-": return n1 - n2
#         case "*": return n1 * n2
#         case "/": return n1 / n2

# n1 = float(input("Enter first number: "))
# op = input("Enter operator (+,-,*,/): ")
# n2 = float(input("Enter second number: "))

# # print(f"{n1} {op} {n2} = ", end="")
# # print(calc(n1, op, n2))   # Output: 1
# print(f"{n1} {op} {n2} = ",calc(n1, op, n2), sep="")

# def is_palindrome(num):
#     num = str(num)
#     rev = num[::-1]
#     print(f"Num: {num}, Rev: {rev}")
#     print(num == rev)

# is_palindrome(12321)

# def is_armstrong(num):
#     # 153 = 1^3 + 5^3 + 3^3
#     sum = 0
#     temp = num
#     length_num = len(str(num))

#     while temp > 0: 
#         digit = temp % 10
#         sum += digit ** length_num
#         temp //= 10
#     print(sum)
#     return num == sum

# print(is_armstrong(92727))
    
# def pyramid(num):
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
#     for i in range(num, 0, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
'''
      *
     ***
    *****
   *******
  *********
 ***********
  *********
   *******
    *****
     ***
      *
      
      '''

# def pyramid(num):
    
#     for i in range(num+1, 1, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
        
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
# '''
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#  '''

# pyramid(5)

def box(num):
    print("*"*(2*num+3))
    
#     for i in range(num+1):
#         print(" "*(num-i), "*"*(2*i+1))
#         # print(" "*(num-i),f"{i}"*(i))
    
#     for i in range(num, 0, -1):
#         print(" "*(num-i+1), "*"*(2*i-1))
    for i in range(num):
        print("*"," "*(num-i),"*"*(2*i+1), " "*(num-i), "*", sep="")
    for i in range(num-1, 0, -1):
        print("*"," "*(num-i+1),"*"*(2*i-1), " "*(num-i+1), "*", sep="")
    print("*"*(2*num+3))

'''
*************
*     *     *
*    ***    *
*   *****   *
*  *******  *
* ********* *
*  *******  *
*   *****   *
*    ***    *
*     *     *
*************
'''

# box(50)
def box(num):
    
    print("*"*(2*num+3))
    for i in range(num):
        print("*"*(num-i)," ","*"*(2*i+1), " ", "*"*(num-i), sep="")
    for i in range(num-1, 0, -1):
        print("*"*(num-i+1)," ","*"*(2*i-1), " ", "*"*(num-i+1), sep="")
    
    print("*"*(2*num+3))
'''
***********************
********** * **********
********* *** *********
******** ***** ********
******* ******* *******
****** ********* ******
***** *********** *****
**** ************* ****
*** *************** ***
** ***************** **
* ******************* *
** ***************** **
*** *************** ***
**** ************* ****
***** *********** *****
****** ********* ******
******* ******* *******
******** ***** ********
********* *** *********
********** * **********
***********************
'''
box(10)