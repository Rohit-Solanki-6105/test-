'''
5. Write a python program to overload the multiplication (*) operator that can act on objects 
of NUM class having two members as no1 and no2.
'''
class Num:
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def __mul__(self, other):
        # Define the behavior of the multiplication operator (*) with Num objects
        if isinstance(other, Num):
            # If 'other' is also an instance of Num, perform element-wise multiplication
            return Num(self.no1 * other.no1, self.no2 * other.no2)
        elif isinstance(other, (int, float)):
            # If 'other' is a scalar (int or float), multiply each element by the scalar
            return Num(self.no1 * other, self.no2 * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Num' and '{type(other).__name__}'")

    def __rmul__(self, other):
        # Define the behavior when the left-hand operand is a scalar and the right-hand operand is a Num object
        if isinstance(other, (int, float)):
            return Num(self.no1 * other, self.no2 * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: '{type(other).__name__}' and 'Num'")

    def __str__(self):
        # Define how the object should be represented as a string
        return f"Num({self.no1 * self.no2})"


num1 = Num(2, 3)
num2 = Num(4, 5)

result1 = num1 * num2
print("Multiplication of num1 and num2:", result1)

result2 = num1 * 2
print("Multiplication of num1 with scalar:", result2)

result3 = 3 * num2
print("Multiplication of scalar with num2:", result3)

'''
Multiplication of num1 and num2: Num(120)
Multiplication of num1 with scalar: Num(24)
Multiplication of scalar with num2: Num(180)
'''