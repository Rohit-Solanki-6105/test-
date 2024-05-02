# 6. Write a Python function to convert a CamelCase string to snake_case.

def camel_to_snake(camel_case_string):
   snake_case_string = ""
   for i, c in enumerate(camel_case_string):
      if i == 0:
         snake_case_string += c.lower()
      elif c.isupper():
         snake_case_string += "_" + c.lower()
      else:
         snake_case_string += c

   return snake_case_string


print("snake_case: ", camel_to_snake(input("Enter CamelCase: ")))

'''
Enter CamelCase: hiHelo
snake_case:  hi_helo
'''