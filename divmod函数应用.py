day = int(input('Enter days:'))
print('Months={}Days={}'.format(*divmod(day,30)))
#*号用于拆分元组内容，divmod函数会返回num1//num2（21//10=2）,num1%num2（21%10=1）