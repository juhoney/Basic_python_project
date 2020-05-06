a = int(input())

def aware(a):
    if a % 2 == 0:
        return 0
    else:
        return 1

a = aware(a)

if a == 0:
    print("짝수")
else:
    print("홀수")