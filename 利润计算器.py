Money = float(input('请输入本金'))#本金
Rate = float(input('请输入利率'))#利率
Period = float(input('请输入周期'))#周期
year = 0 
while year<int(Period) : #循环结构
    All = Money*Rate+Money
    year+=1
    Money = All
print (' 你的总金为{:.2f}'.format(All))
b=input()
print('按任意键以退出')
    