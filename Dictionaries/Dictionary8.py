# Start with an empty list.
users = []
new_user = {
    'last': 'Mahboob',
    'first': 'Talha',
    'username': 'tmahboob',
 }

users.append(new_user)

new_user = {
    'last': 'Ahmed',
    'first': 'Ali',
    'username': 'aahmed',
 }
users.append(new_user)

for user in users:
    for k, v in user.items():
        print(k + ": " + v)
        print("\n")