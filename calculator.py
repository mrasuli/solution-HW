def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def read_numbers():
    while True:
        num_str = input("please enter your number: ")
        if num_str.isdigit():
            num = int(num_str)
            return num
            break
        elif num_str == "stop":
            return num_str
            break
        else:
            print("Please enter correct number: ")


def read_operation():
    operations = ["+", "/", "*", "-"]
    while True:
        op_str = input('Please enter the operation ("+", "/", "*", "-"): ')
        if op_str in operations:
            op = op_str
            return op
            break


if __name__ == '__main__':  # ctr alt l
    while True:
        num1 = read_numbers()
        if num1 == "stop":
            break
        num2 = read_numbers()
        op = read_operation()
        if op == "/":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif op == "*":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif op == "+":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif op == "-":
            print(f"{num1} - {num2} = {multiply(num1, num2)}")
