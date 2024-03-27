import random

start = input('請輸入數字範圍起始值: ')
end = input('請輸入數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start , end)
count = 0

while True:
    count += 1
    num = input('請輸入數字: ')
    num = int(num)
    if num == r:
        print('答案就是', r)
        print('你總共猜了' , count ,'次')
        break
    elif num > r:
        print('比' , num , '小')
    else:
        print('比' , num , '大')
    print('你已經猜', count, '次')
