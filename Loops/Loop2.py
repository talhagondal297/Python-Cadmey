# While Loop
# a = 15

# while True:
#     print(a)

# =============================

# program to calculate the sum of numbers
# until the user enters zero
total = 0
number = int(input("Enter a number : "))
while number!=0:
    total = total +number
    number = int(input("Enter a number:"))
print("Total =" , total) 