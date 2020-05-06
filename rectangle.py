x,y,w,h = map(int, input().split())
up_y = h - y
down_y = y
right_x = w - x
left_x = x

min_y = up_y
min_x = left_x
if up_y > down_y:
    min_y = down_y
if left_x > right_x:
    min_x = right_x

if min_x >= min_y:
    print(min_y)
else:
    print(min_x)




