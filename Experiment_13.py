# Write a program to find left shift and right shift values of a given number.

n = int(input("Enter a number: "))
shift = int(input("Enter number of bits to shift: "))

print("Left shift value:", n << shift)
print("Right shift value:", n >> shift)