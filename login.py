from getpass import getpass

account = '10401703'
password = '123456'
i = 3

while i > 0:
    i = i - 1
    login_name = input('input your name: ')
    login_paas = getpass('input your password: ')
    if login_name == account and login_paas == password: 
        print('login successed')
        break
    else:
        print('Wrong account or password!')
        if i > 0:
            print('you still have', i ,'time to retry。')
        else:
            break


