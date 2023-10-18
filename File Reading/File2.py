# Opening and reading txt file

file = "File Reading\File1.txt"

with open(file, 'r') as f:
    lines = f.readlines()

for x in lines:
    print(x)

file2 = "File Reading\File2.txt"

with open(file2, 'r') as f:
    lines = f.readlines()

for x in lines:
    print(x)

    
import os

print("Current Working Directory:", os.getcwd())
