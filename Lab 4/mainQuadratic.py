from quadratic import *

a, b, c = [int(i) for i in input("Enter the coefficients a b c (separate them with a space)\n").split()]
quadratic_equation = Quadratic(a,b,c)

if(quadratic_equation.get_discriminant() > 0):
    print("There are two roots.",\
          "\n\t\tRoot1: ", quadratic_equation.get_root1(),\
          "\n\t\tRoot2: ", quadratic_equation.get_root2())
elif(quadratic_equation.get_discriminant() == 0):
    print("There is one root:", quadratic_equation.get_root1())
else:
    print("The equation has no roots")