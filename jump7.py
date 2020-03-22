for i in range(1,101):
    string=str(i)
    if i%7==0:
        continue
    elif string[-1]=='7' or string[0]=='7' :
        continue
    else:
        print(i)
print('请按任意键退出。')
a=input()