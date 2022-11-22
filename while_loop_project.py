
# Constructing while loops that gives the user to enter username and password with 5 attempts.
user = 'Mike'
pwd = '1234'
attempts = 0
while attempts < 6:
    attempts += 1
    username = input('username: ')
    password = input('password: ')

    if username == user and password == pwd:
        print('you are in!')
        break
    elif username != user and password != pwd:
        if attempts < 5:
            print('incorrect, Try again! ')
        else:
            print('Account blocked, too many attempts')
            break
