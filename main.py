def CRUD():

    user = {
        'a' : '1',
        'b' : '2',
        'c' : '3',
        'd' : '4',
        'e' : '5'
    }
    # 1. Функція без параметрів. Додає юзера до словника
    login = str(input('Enter your login -> '))
    password = str(input('Enter your password -> '))

    question = input('Do you want to register? ')
    if question == 'Yes' or 'yes':
        user[login] = password
    else:
        print('Bye!')
    print(user)

    # 2. Функція без параметрів. Змінює пароль юзера, якщо він все ввів та хоче змінити
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

    # 3. Функція без параметрів. видаляє юзера з словника, якщо він там є
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

    # 4. Функція без параметрів. Видаляє юзерів зі словника
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
