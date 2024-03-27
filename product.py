product = []

while True:
    name = input('請輸入產品名稱: ')
    if name == 'q':
        break
    price = input('請輸入產品價格: ')
    p = []
    p.append(name)
    p.append(price)
    product.append(p)
print(product)