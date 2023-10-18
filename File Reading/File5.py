# Creating txt file and adding data from other txt file

file = "File Reading\File3.txt"

with open(file, 'r') as f:
    lines = f.readlines()


with open("File4.txt", 'w+') as f:
    for line in lines:
        f.write(line)