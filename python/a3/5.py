# 5. Write a Python function to count the number of words in a given string.

def count_words(s):
    return len(s.split())

print("Total words: ", count_words(input("Enter String: ")))

'''
Enter String: hi helo
Total words:  2
'''