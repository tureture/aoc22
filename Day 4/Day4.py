

counter = 0

'''
with open('Day 4/Day4_2.txt') as f:
    for i in f:
        t = i.strip().split(',')
        big_list = t[0] + '-' + t[1]
        separated_values = big_list.split('-')
        n1 = int(separated_values[0])
        n2 = int(separated_values[1])
        n3 = int(separated_values[2])
        n4 = int(separated_values[3])

        if n1 <= n3 and n2 >= n4 or n1 >= n3 and n2 <= n4:
            counter += 1
'''

with open('Day 4/Day4.txt') as f:
    for i in f:
        t = i.strip().split(',')
        big_list = t[0] + '-' + t[1]
        separated_values = big_list.split('-')
        n1 = int(separated_values[0])
        n2 = int(separated_values[1])
        n3 = int(separated_values[2])
        n4 = int(separated_values[3])

        #if n1 <= n3 or n2 >= n4 or n1 >= n3 or n2 <= n4:
          #  counter += 1

        if n1 <= n3 <= n2 or n1 <= n4 <= n2 or n3 <= n1 <= n4 or n3 <= n2 <= n4:
            counter += 1
#[n1 - n2]

#[n3 - n4]

#n1 < n3 < n2 or n1 < n4 < n2 or n3 < n1 < n4 or n3 < n2 < n4

print(counter)

# 507

