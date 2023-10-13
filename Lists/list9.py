a = ["Talha", "is a student ", "Of Ai", 2+2j]

a[2] = "Of Ai Cadmey"
a[3] = 14+3j
a.append('Mahboob')

print(a)
# printing list items
num1 = [14,3,'talha',1060]
print(num1)
# printing length of list 
print("Length of List is" ,len(num1))
#  getting value of index 2
print(num1[2])
print(num1[-2])
#  insert an item to list
num1.insert(1,8)
print(num1)
#  remove an item to list
num1.remove(1060)
print(num1)
#  pop an item to list
num1.pop(3)
print(num1)
#  sort the list
num1.sort()
print(num1)
# One list extend to other
num1.extend([3,54,4,24,1,44])
print(num1)
#  Minimum number of list
print(min(num1))
#  Maximum number of list
print(max(num1))
#  Sum of list
print(sum(num1))