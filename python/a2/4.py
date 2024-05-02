'''
4. Write a python program to create employee class that has employee details (id, name, 
salary) and design a function that reads the employee id from the user and display employee 
details along with the Net salary after adding DA(15%), MA(5%), HRA(20%) and deducting 
PA(12%) from the basic salary.
'''

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_net_salary(self):
        # Constants for percentage values
        da_percent = 15
        ma_percent = 5
        hra_percent = 20
        pa_percent = 12

        # Calculate allowances and deductions
        da_amount = (da_percent / 100) * self.salary
        ma_amount = (ma_percent / 100) * self.salary
        hra_amount = (hra_percent / 100) * self.salary
        pa_amount = (pa_percent / 100) * self.salary

        # Calculate net salary
        net_salary = self.salary + da_amount + ma_amount + hra_amount - pa_amount

        # Display employee details and net salary
        print("\nEmployee Details:")
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.salary)
        print("DA (15%):", da_amount)
        print("MA (5%):", ma_amount)
        print("HRA (20%):", hra_amount)
        print("PA (12%):", pa_amount)
        print("Net Salary:", net_salary)



# Create an employee object
emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")
salary = float(input("Enter Basic Salary: "))

employee = Employee(emp_id, name, salary)

# Calculate and display net salary
employee.calculate_net_salary()

'''
Enter Employee ID: 1
Enter Employee Name: hi
Enter Basic Salary: 100

Employee Details:
Employee ID: 1
Name: hi
Basic Salary: 100.0
DA (15%): 15.0
MA (5%): 5.0
HRA (20%): 20.0
PA (12%): 12.0
Net Salary: 128.0
'''