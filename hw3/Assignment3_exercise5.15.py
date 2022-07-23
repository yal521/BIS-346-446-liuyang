from operator import itemgetter 
# tuple invoice created using sample data
invoice = (('83','Electric sander',7,57.98),('24','power saw',18,99.99),
('7','sledge hammer',11,21.50),('77','Hammer',76,11.99),
('39','Jig Saw',3,79.50))

print("invoice sorted by item description")
print(sorted(invoice,key=itemgetter(1))) #sorting invoice data according to the description
print("invoice sorted by item price")
print(sorted(invoice,key=itemgetter(3))) #sorting invoice data according to the price
print('------------invoice tuple containing part description and quantity---------------')
x = () # empty tuple to store data
for i in invoice: # for each tuple inside invoice tuple
 temp1 = ((i[1],i[2])) #temporary tuple containing mapping between (description,quantity)
x += (temp1,) # add this tuple to x
print(sorted(x,key=itemgetter(1))) # sorting tuple x according to the quantity
print('------------invoice tuple containing part description and value------------------')
y = () #empty tuple
for i in invoice: # for each tuple inside invoice tuple
 temp2 = (i[1],i[2]*i[3]) #temporary tuple containing mapping between (description,value)
y += (temp2,) # adding this temporary tuple to y
print(sorted(y,key=itemgetter(1))) # sorting tuple y according to the value

#filtering the results of for the the values between 200 and 500
for i in y:
 if i[1]>=200 and i[1]<=500:
    print(i)

total = 0 # variable to store total amount
for i in y:
    total += i[1] # add value of each item to total
print("total value is ",total) # display total