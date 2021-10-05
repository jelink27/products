products = []
cost = []

while True:    #在不知道會執行幾次的時候通常用while
    name = input('請輸入商品名稱：')
    if name == 'q': #quit
        break
    price = input('請輸入商品價格:')
    #p = [] #這3行也可以寫成p = [name, price]
    #p.append(name) #把name裝進p裡面
    #p.append(price) #把price裝進p裡面
    #products.append(p) #把p裝進大清單
    products.append([name, price])
    
    
   
    
print(products) 
products[0][0] #第0格的第0格 存取是第一個index的第一個