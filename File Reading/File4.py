# Creating and add data in txt file

file = "File Reading\File3.txt"

with open(file, 'w+') as f:
    f.write("Hello World!")
    
# Reading File3.txt File   
file = open("File Reading\File3.txt", "r")
print(file.read())