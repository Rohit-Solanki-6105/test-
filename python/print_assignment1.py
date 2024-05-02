import os

# Open the output file in write mode
with open('print_assignment.txt', 'w') as f:
    # Iterate over all files in the current directory
    for filename in os.listdir('.'):
        # Check if the file is a Python file
        if filename.endswith('.py'):
            # Open the file in read mode
            with open(filename, 'r') as file:
                # Read the contents of the file
                contents = file.read()
                
                f.write('\n')
                # Write the contents to the output file
                f.write(contents)
                # Add a blank line between files
                f.write('\n-------------------------------------------------------\n')

print("Python files have been written to print_assignment.txt")