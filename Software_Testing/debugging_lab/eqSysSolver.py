def lcm(a, b):
    # Check if numbers are valid (not 0)
    if a == 0 or b == 0:
        return 0
    
    
    # Find the maximum of two numbers
    max_num = max(a, b)

    # Find the LCM by iterating from the maximum number
    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break
        max_num += 1

    return lcm


# print(lcm(int(input("Enter the first number: ")), int(input("Enter the second number: "))))

#Ask for the firyst equation from the system
eq1 = input("Enter the first equation (xval yval result): ")
eq2 = input("Enter the second equation (xval yval result): ")


#Split the equations into lists
eq1 = eq1.split()
eq2 = eq2.split()

#If there is less than 3 values in the equations, add 0 until there are 3 values
while len(eq1) < 3:
    eq1.append(0)

while len(eq2) < 3: 
    eq2.append(0)

#Print the equations in a readable format
print("Equation 1:", eq1[0], "x +", eq1[1], "y =", eq1[2])
print("Equation 2:", eq2[0], "x +", eq2[1], "y =", eq2[2])

#Convert the strings to integers
eq1 = [int(i) for i in eq1]
eq2 = [int(i) for i in eq2]

#Solve the system of equations
# x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
# y = (a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1)

#Check if the denominator is 0, if it is, the system is unsolvable
if (eq1[0] * eq2[1] - eq2[0] * eq1[1] == 0) or (eq1[0] * eq2[1] - eq2[0] * eq1[1] == 0):
    print("The system is unsolvable.")
    exit()
    
x = (eq1[2] * eq2[1] - eq2[2] * eq1[1]) / (eq1[0] * eq2[1] - eq2[0] * eq1[1])
y = (eq1[0] * eq2[2] - eq2[0] * eq1[2]) / (eq1[0] * eq2[1] - eq2[0] * eq1[1])

#If the values are decimals, express them as fractions
if x % 1 != 0:
    x = str(x)
    x = x.split(".")
    x = [int(i) for i in x]
    x = x[0] / lcm(x[0], x[1])

if y % 1 != 0:
    y = str(y)
    y = y.split(".")
    y = [int(i) for i in y]
    y = y[0] / lcm(y[0], y[1])

print("x =", x)
print("y =", y)
