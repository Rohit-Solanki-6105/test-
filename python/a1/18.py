# 18) Write a python program to find binary value of a character.
# bin_val = bin(ord(input("Enter a Character: ")))
# bin_value = str(bin_val)
# print(bin_value)

def Print_Binary_Values(num): 
    # base condition 
    if(num > 1): 
        Print_Binary_Values(num // 2) 
    print(num % 2, end="") 

# Rohit
Print_Binary_Values(ord('R'))
print(end=" ")
Print_Binary_Values(ord('o'))
print(end=" ")
Print_Binary_Values(ord('h'))
print(end=" ")
Print_Binary_Values(ord('i'))
print(end=" ")
Print_Binary_Values(ord('t'))

'''
1010010 1101111 1101000 1101001 1110100
'''