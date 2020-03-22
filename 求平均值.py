N = int(input('你要输入的数字的数量'))
sum=0.0
count = 0
while count<N:
    count=count+1
    In=float(input('第{}个数'.format(count)))
    sum+=In
average=sum/N
print('平均值为{}'.format(average))

