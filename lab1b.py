# a) name variable to input username
name = input("Enter your name: ")
# b) enter x value as input to variable xStr
xStr = input("Enter x value: ")
# d) convert value to integer in variable x
x = int(xStr)
# c) enter y value as input to variable yStr
yStr = input("Enter y value: ")
# d) convert value to integer in variable y
y = int(yStr)
# e) Arithmetic Operators of x & y variables
total = (x + y)
diff = (x - y)
prod = (x * y)
div = (x / y)
# f) Print statements to display variables
print(name,"your calculations are:\n",
    x,"+",y,"=", total,"\n",
      x,"-",y,"=", diff,"\n",
        x,"*",y,"=", prod,"\n",
            x,"/",y,"=", div,"\n\nThe calculations are complete")

# g) float() will lead to decimal places of the outcome which will not show up in the int() function
# for eg, prod function will return 80.0 in float and 80 in integer data type