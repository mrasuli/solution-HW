
# Read how many employees you need to enter?
employee_count_str = input("please enter how many employees you have: ")
employee_count = int(employee_count_str)
for employee_index in range (employee_count):
# loop through employees
# Read first name, last name, and age
    while True:
        first_name = input("please enter the first name: ")
        if len(first_name.strip()) > 0:
            break
    last_name = input("please enter your last name: ")
    age_str = input("please enter your age: ")
    age = int(age_str)
    print(f"Employee data: First Name: {first_name}, Last Name: {last_name}, Age: {age}")
#

# check first name and last name are not empty

# check that employees are in between age 18 and 100

# Check the total age is not more than 500
