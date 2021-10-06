products = []
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
#products[0][0] #第0格的第0格 存取是第一個index的第一個   
    
print(products) 

for p in products:
    print(p[0],'的價格是',p[1]) #每一個清單的第0格存名稱 1存價格

with open('product.csv', 'w') as f: #打開這個檔案 寫入product.csv檔 如果沒有會創建 如果有會覆蓋
    for p in products:              #with在使用完後會自動關閉，不會夾住檔案
        f.write(p[0] + ',' + p[1] + '\n') #用.write 寫進f裡面 通常最後會用換行做合併 在csv裡面才會換行

