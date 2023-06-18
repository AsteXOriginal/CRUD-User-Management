def CRUD():

    user = {
        'a' : '1',
        'b' : '2',
        'c' : '3',
        'd' : '4',
        'e' : '5'
    }
    # 1. A function without parameters. Adds a user to the dictionary
    login = str(input('Enter your login -> '))
    password = str(input('Enter your password -> '))

    question = input('Do you want to register? ')
    if question == 'Yes' or 'yes':
        user[login] = password
    else:
        print('Bye!')
    print(user)

    # 2. A function without parameters. Changes the user's password if he has entered everything and wants to change it
    login = str(input('Enter your login -> '))
    password = str(input('Enter your password -> '))

    if login in user and user[login] == password:
        question = input('Do you want to change your password? ')
        if question == 'Yes' or 'yes':
            newPassword = input('New password -> ')
            user[login] = newPassword 
        else:
            print('Bye!')
        print(user)
    else:
        print('Error!')

    # 3. A function without parameters. removes the user from the dictionary, if it exists
    login = str(input('Enter your login -> '))
    password = str(input('Enter your password -> '))

    if login in user and user[login] == password:
        question = input('Do you want to exit the database? ')
        if question == 'Yes' or 'yes':
            del user[login]
        else:
            print('Bye!')
        print(user)
    else:
        print('Error!')

    # 4. A function without parameters. Removes users from the dictionary
    login = str(input('Enter your login -> '))
    password = str(input('Enter your password -> '))
    
    if login in user and user[login] == password:
        question = input('Do you want to clear the database? ')
        if question == 'Yes' or 'yes':
            user.clear()
        else:
            print('Bye!')
        print(user)
    else:
        print('Error!')

CRUD()
