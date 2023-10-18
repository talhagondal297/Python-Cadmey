def function(x= '10', y = '7'):
    sum = int(x) + int(y)
    return sum


num1 = input("Enter 1st Number: ")
num2 = input("Enter 2nd Number: ")

result = function(num1, num2)

print(result)