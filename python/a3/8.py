# 8. Write a Python function to count the frequency of a substring within a string.

def freq_sub(sub, string):
    counter = 0
    for i in range(len(string) - len(sub)):
        if sub == string[i:i+len(sub)]:
            counter += 1

    return counter

string = input("Enter String: ")
substr = input("Enter substring: ")

print("Total frequency: ", freq_sub(substr, string))

'''
Enter String: hi hihelo whatsup
Enter substring: hi
Total frequency:  2
'''