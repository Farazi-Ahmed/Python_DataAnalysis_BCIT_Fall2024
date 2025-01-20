'''
		Function: Identifying Floor Divisions with operator '//'
    :param integers a and b
    :return: the floor division when number a is divided by number b
'''

def calNumbers_Floor_division (a,b):
    return int(a)//int(b)
print('The number is', calNumbers_Floor_division(input(),input()))

------------------------------------------------------------------------------------

'''
    Function: Addition of two integers along with specifying their data types
    :param integers a and b
    :return addition of integers a and b
    :rtype integer
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)
print(type(num1),type(num2))
print("first no:",str(num1))
print("second no:",str(num2))

------------------------------------------------------------------------------------

# To print on the same line use the end function in print()
print("Hello World!",end=",")
print("Hello World2",end=",")

------------------------------------------------------------------------------------

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Main function to run
if __name__ == '__main__':
    print_hi('PyCharm')
