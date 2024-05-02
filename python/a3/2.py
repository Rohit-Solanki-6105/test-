# 2. Write a Python function to count the number of vowels in a given string

def vowel_counter(string):
    counter = 0
    for c in string:
        for vowel in "aeiouAEIOU":
            if c == vowel: 
                counter+=1
    
    return counter

string = input("Enter string: ")

print(f"Total vowels: {vowel_counter(string)}")

'''
Enter string: hihElo
Total vowels: 3
'''