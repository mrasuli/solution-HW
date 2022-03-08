
# Read how many employees you need to enter?
employee_count_str = input("please enter how many employees you have: ")
employee_count = int(employee_count_str)
total_age = 0
for employee_index in range (employee_count):
# loop through employees
# Read first name, last name, and age
    while True:
        first_name = input("please enter the first name: ")
        if len(first_name.strip()) > 0:
            break
    while True:
        last_name = input("please enter your last name: ")
        if len(last_name.strip()) > 0:
            break
    while True:
        age_str = input("please enter your age: ")
        if age_str.isdigit():
            age = int(age_str)
        if age >= 18 and age <= 100:
            total_age = total_age + age
            break
        else:
            print("The age should be a digit between 18 and 100: ")

    print(f"Employee data: First Name: {first_name}, Last Name: {last_name}, Age: {age}")
    print(f"Total age = {total_age}")
if total_age > 500:
    print("Warning the total age is less than 500")
# when calculating age inside the loop

# check first name and last name are not empty

# check that employees are in between age 18 and 100

# Check the total age is not more than 500
