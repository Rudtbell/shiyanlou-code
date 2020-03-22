import time
import random
name=input('请输入你的名字')
level=int(input('请输入你的等级'))
HP=level*40
str=level*10
defend=level*1
hp_boss=10000
str_boss=100
print('现在开始干架吧{}'.format(name))
while hp_boss>=0:
    rate=random.randint(1,2)
    a=str_boss*rate
    HP=HP-a
    print ('boss对{}造成了{:.2f}点伤害，你剩余{:.2f}点血'.format(name,a,HP))
    a=a/rate
    time.sleep(0.2)
    if HP<=0:
        print('你挂了')
        break    
    elif HP>0:
        b=str*rate        
        hp_boss=hp_boss-b
        print ('{}对boss造成{:.2f}点伤害，boss剩余{:.2f}血'.format(name,b,hp_boss))
        time.sleep(0.2)
        b=b/rate
        if hp_boss<=0:
            break        
if HP>0:
    print('{}战胜了boss'.format(name))
print('按任意键以退出。')
input()
