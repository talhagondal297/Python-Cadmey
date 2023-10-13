# Breaking While Loop

a = 10

while True:
    print(a)
    break

#  While loop with Break statement 
counter = 0
while counter < 3:
    if counter == 1:
        break
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')


# Continue While Loop

a = 10

while True:
    if a>9:
        print(a + 10)
    continue
    