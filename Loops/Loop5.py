# Removing values using while loop

pets = ['dog', 'cat', 'dog', 'fish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print("After removing cat from list: " ,pets)
   
while 'dog' in pets:
    pets.remove('dog')   

print("After removing dog from list: ",pets)