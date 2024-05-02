'''
2. Define class student with attributes like First_name, Last_name, Course, batch_year, result). 
Apply constructor (s) to initialize the attributes while creating new student object. Here, 
batch_year must be passing year and result must be PASS or FAIL. Add a method to calculate 
total number of FAIL students. (static method).
'''
class Student:
    def __init__(self, First_name, Last_name, Course, batch_year, result):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Course = Course
        self.batch_year = batch_year
        self.result = result

    @staticmethod
    def count_fail_students(students):
        return len([student for student in students if student.result == 'FAIL'])
    

# Example usage:
students = [
    Student('hi', 'helo', 'CS', 2020, 'PASS'),
    Student('just', 'kidding', 'CS', 2020, 'FAIL'),
    Student('no', 'never', 'CS', 2020, 'PASS'),
    Student('workin', 'progress', 'CS', 2020, 'FAIL'),
]

num_fail_students = Student.count_fail_students(students)
print(f'Number of FAIL students: {num_fail_students}')

'''
Number of FAIL students: 2
'''