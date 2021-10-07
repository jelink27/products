import os #載入operating system
products = []

#讀取檔案
if os.path.isfile('product.csv'): #path模組的isfile功能 檢查檔案在不在
    print('找到檔案')
    with open('product.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue #商品價格出現在line裡面時，跳到下一回
            name, price = line.strip().split(',')  #.strip()去除換行符號， 再用,來切割 讀取先前寫入的檔案 存進name跟price
            products.append([name, price])
            
else:
    print('找不到檔案')

#使用者輸入
while True:    #在不知道會執行幾次的時候通常用while
    name = input('請輸入商品名稱：')
    if name == 'q': #quit
        break
    price = input('請輸入商品價格:')
    price = int(price) #price轉換成整數 但轉換後+法不能合併
    products.append([name, price])
    print(products)
    #p = [] #這3行也可以寫成p = [name, price]
    #p.append(name) #把name裝進p裡面
    #p.append(price) #把price裝進p裡面
    #products.append(p) #把p裝進大清單
    #products[0][0] #第0格的第0格 存取是第一個index的第一個   

#印出所有購買紀錄
for p in products:
    print(p[0],'的價格是',p[1])                         #每一個清單的第0格存名稱 1存價格

#寫入檔案    
with open('product.csv', 'w',encoding='utf-8') as f:    #打開這個檔案 寫入product.csv檔 如果沒有會創建 如果有會覆蓋  
    f.write('商品,價格\n')                              #後面那行意思為 寫入這個檔案用的編碼為utf-8
    for p in products:                                  #with在使用完後會自動關閉，不會夾住檔案
        f.write(p[0] + ',' + str(p[1]) + '\n')          #用.write 寫進f裡面 通常最後會用換行做合併 在csv裡面才會換行
                                                        #前面多了把price轉換成數字 數字不能跟字串合併 必須轉換成str字串

