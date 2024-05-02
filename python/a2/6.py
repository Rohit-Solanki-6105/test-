'''
6. Write a python program to create class time with attributes hour and minutes. Add 
constructor(s) to initialize the attributes. Overload '+' operator to add two time (hh:mm) 
type objects to show new added time.
'''

class Time:
    def __init__(self, hour=0, minutes=0):
        self.hour = hour
        self.minutes = minutes

    def __add__(self, other):
        # Check if 'other' is also a Time object
        if isinstance(other, Time):
            # Calculate total minutes
            total_minutes = self.minutes + other.minutes
            carry_hour = total_minutes // 60  # Calculate hours to carry over
            final_minutes = total_minutes % 60  # Calculate final minutes after carrying over

            # Calculate total hours
            total_hours = self.hour + other.hour + carry_hour

            return Time(total_hours, final_minutes)
        else:
            # Raise TypeError if 'other' is not a Time object
            raise TypeError("Unsupported operand type(s) for +: 'Time' and '{}'".format(type(other).__name__))

    def __str__(self):
        # Format the time as hh:mm
        return f"{self.hour:02}:{self.minutes:02}"


time1 = Time(3, 45)
time2 = Time(1, 30)

# Adding two Time objects using the '+' operator
result_time = time1 + time2
print("Sum of time1 and time2:", result_time)

'''
Sum of time1 and time2: 05:15
'''
