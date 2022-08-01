import timeit
import random
import numpy
counts = [10**x for x in range(0,7)];
def gen_list(size):
    l = []
    for i in range(size):
        l.append(random.randint(0,7))
        
def gen_array(size):
    l = numpy.random.rand(size)
    
print("Number of values\t List average execution time\t Array average execution time ")
for i in counts:
    
    list_timer = timeit.Timer(lambda: gen_list(i))
    array_timer = timeit.Timer(lambda: gen_array(i))
    print(f"{i}\t\t\t\t {list_timer.timeit(5)}\t\t {array_timer.timeit(5)}")

