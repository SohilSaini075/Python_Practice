#Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.


a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))


c = (a**2 + b**2) ** 0.5


print("The length of the hypotenuse is:", c)
