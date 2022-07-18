principal = 1000
rate = 7
rate = rate/100
d= {}
number =[10,20,30]
for number in number :
    d['Amount after {0} years'.format(number)]=principal * pow( 1+rate, number)
print(d)