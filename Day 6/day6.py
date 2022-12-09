
'''
n1 = ""
n2 = ""
n3 = ""
n4 = ""
counter = 0

with open('Day 6/day6.txt') as f:
    data = f.readline()
    n1 = data[3]
    n2 = data[2] 
    n3 = data[1]
    n4 = data[0]

    for i in range(len(data)+4):
        counter = i

        n4, n3, n2 = n3, n2, n1
        n1 = data[i]
        x = [n1, n2, n3, n4]
        print(x)
        if len(x) == len(set(x)):
            break
print(i+1)  

'''

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

counter = 0
print(n)
with open('Day 6/day6.txt') as f:
    data = f.readline()
    for i in range(14):
        n[i] = data[i]




    for i in range(len(data)+14):
        counter = i

        for j in range(14):
            n[j] = data[i+j]

        if len(n) == len(set(n)):
            break
print(i+14)   

