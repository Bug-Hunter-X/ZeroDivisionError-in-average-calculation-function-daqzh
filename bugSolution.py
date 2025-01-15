def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

#Alternative solution using try-except block
def calculate_average_try_except(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return 0 #or handle the exception in a different way

my_list = [1,2,3,4,5]
result = calculate_average_try_except(my_list)
print(f"The average is: {result}")
my_empty_list = []
result = calculate_average_try_except(my_empty_list)
print(f"The average is: {result}")    