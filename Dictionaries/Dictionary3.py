# Looping Through Numbers
favourite_numbers = {'Talha': 7, 'Samsaam': 9}

for name in favourite_numbers.keys():
    print(name + ' loves a number')
    
# ===============


# Looping Through Numbers
favourite_numbers = {'Talha': 7, 'Samsaam': 9}

for name, number in favourite_numbers.items():
    print(name + ' loves the number ' + str(number))