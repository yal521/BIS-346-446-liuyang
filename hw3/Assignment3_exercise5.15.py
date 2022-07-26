from operator import itemgetter 
# tuple invoice created using sample data
invoice = (('83','Electric sander',7,57.98),
           ('24','power saw',18,99.99),
           ('7','sledge hammer',11,21.50),
           ('77','Hammer',76,11.99),
           ('39','Jig Saw',3,79.50))

print("invoice sorted by item description")
for part, desc, quant, price in sorted(invoice, key=itemgetter(1)):
    print(f'{part:>2}  {desc:<20}{quant:>3}{price:7.2f}')
    
print("invoice sorted by item price")
for part, desc, quant, price in sorted(invoice, key=itemgetter(3)):
    print(f'{part:>2}  {desc:<20}{quant:>3}{price:7.2f}')
    
print("desc and quant")
quantities = [(desc, quant) for part, desc, quant, price in invoice]
for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<24}{quant:>3}')
    
print("desc and value")
prices = [(desc, quant * price) for part, desc, quant, price in invoice]
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<22}{total:9.2f}')
    
print("value in [200,500]")   
prices = [(desc, quant * price) for part, desc, quant, price in invoice\
          if 200 <= quant * price <= 500]
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<22}{total:9.2f}')

print("total value")  
prices = [(desc, quant * price) for part, desc, quant, price in invoice]
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<22}{total:9.2f}')
total = sum([(quant * price) for part, desc, quant, price in invoice])
print(f'Total for all is:       {total:.2f}')