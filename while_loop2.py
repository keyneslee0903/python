while True:
    mode = input('請輸入遊戲模式： ')
    if mode == 'q':
        break
    elif mode == '1':
        print('啟動模式1')
    elif mode == '2':
        print('啟動模式2')
    else:
        print('只能輸入 1/2/q')
