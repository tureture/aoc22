import numpy as np
import math

maximum = 0
nr_2 = 0
nr_3 = 0
running_sum= 0
prev = "\n"

with open('day1.txt') as f:
    lines = f.readlines()

with open('day1.txt') as f:
    for line in f:
        l = line.strip()

        if l != "":
            running_sum += int(l)
        else:
            if running_sum >= maximum:
                nr_3 = nr_2
                nr_2 = maximum
                maximum = running_sum
            elif running_sum >= nr_2:
                nr_3 = nr_2
                nr_2 = running_sum
            elif running_sum > nr_3:
                nr_3 = running_sum



            running_sum = 0
                  
    
print(maximum)
print(nr_2)
print(nr_3)
print(nr_3+nr_2+maximum)