
# implement a program in Python that prompts the user for mass as an integer (in kilograms) and
# then outputs the equivalent number of Joules as an integer.
# Assume that the user will input an integer.

# m = (50)
# t = 300000000
# c = (t * t)

# formalu = m * c

def energy():
    mass = int(input("m: "))
    t = 300000000
    c = (t * t)
    e = mass * c
    print("E:", e)

energy()


# print(formalu)
# def einstein():
#     e = int(input("m: "))
#     print("E:", e)

# def mass(m):
#     t = 300000000
#     c = (t * t)
#     return m * c

