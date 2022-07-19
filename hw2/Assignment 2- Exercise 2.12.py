principal = 1000.0
rate = 0.07

for year in [10,20,30]:
    print(f'Amount after {year} year(s): {principal * (1 + rate) ** year:.2f}')
