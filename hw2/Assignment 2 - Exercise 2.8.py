print(' number square cube')
for x in range(0, 6):
  print('{:< 7d}{:< 7d}{:< 7d}'.format(x, x*x, x*x*x))
print(' number square   cube')
for x in range(0, 6):
  print('{:> 7d}{:> 7d}{:> 7d}'.format(x, x*x, x*x*x))