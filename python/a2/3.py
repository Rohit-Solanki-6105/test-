'''
3. Define class Surface_Area which includes three methods with the name Calculate_area() 
(Function Overloading). Each method accepts parameter(s) to calculate area of circle, 
rectangle and triangle. Display the result from calling of respective Calculate_area() as per 
the user’s request. Design the menu-driven program.
'''

# class Surface_Area:

#     def Calculate_area(self, length, breadth):
#         return length * breadth

#     def Calculate_area(self, base, height, default=1):
#         return 0.5 * base * height
    
#     def Calculate_area(self, radius):
#         return 3.14 * radius ** 2


class Surface_Area:

    def Calculate_area(self, *args):
        if len(args) == 1:
            # Calculate area of circle (args[0] = radius)
            radius = args[0]
            return 3.14 * radius ** 2
        elif len(args) == 2:
            # Calculate area of rectangle (args[0] = length, args[1] = breadth)
            length, breadth = args
            return length * breadth
        elif len(args) == 3:
            # Calculate area of triangle (args[0] = base, args[1] = height, args[2] = default)
            base, height, _ = args  # Ignore the third argument (default)
            return 0.5 * base * height
        else:
            raise ValueError("Invalid number of arguments")

def main():
    surface_area = Surface_Area()
    while True:
        print("-----------------------------------")
        print("1. Calculate area of circle")
        print("2. Calculate area of rectangle")
        print("3. Calculate area of triangle")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        print("-----------------------------------")
        if choice == 1:
            radius = float(input("Enter radius: "))
            print("Area of circle:", surface_area.Calculate_area(radius))
        elif choice == 2:
            length = float(input("Enter length: "))
            breadth = float(input("Enter breadth: "))
            print("Area of rectangle:", surface_area.Calculate_area(length, breadth))
        elif choice == 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            print("Area of triangle:", surface_area.Calculate_area(base, height, 1))
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

main()

'''
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 1
-----------------------------------
Enter radius: 2
Area of circle: 12.56
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 2
-----------------------------------
Enter length: 2
Enter breadth: 3
Area of rectangle: 6.0
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 3
-----------------------------------
Enter base: 5
Enter height: 6
Area of triangle: 15.0
-----------------------------------
1. Calculate area of circle
2. Calculate area of rectangle
3. Calculate area of triangle
4. Exit
Enter your choice: 4
-----------------------------------
'''