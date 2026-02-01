# Write a program to print truth table for bitwise operators (&, | and ^ operators)

print("A B  A&B  A|B  A^B")
for A in [0, 1]:
    for B in [0, 1]:
        print(A, B, " ", A & B, "   ", A | B, "   ", A ^ B)