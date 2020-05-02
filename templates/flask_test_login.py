n = ['hello', 'program', 'login']
m = ['hi', 'program', 'login']

a = input()
b = input()
flag = 0

def check_test(a, b, flag, n, m):
    for i in range(len(n)):
        if a == n[i] and b == m[i]:
            flag = 1
    if flag == 1:
        print('username_password_login well')
    else:
        print('can`t found')

check_test(a, b, flag, n, m)