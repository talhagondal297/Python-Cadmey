# Using Positional Arguments

def describe_pet(animal = 'hamster', name = 'None'):
    # Doc String 
    """Display information about a pet.""" 
    print("\nI have a " + animal + ".")
    print("Its name is " + name + ".")


describe_pet('Horse', 'lion')
describe_pet('dog', 'Cat')

describe_pet()
describe_pet(animal='Snack', name='Rabbit')
