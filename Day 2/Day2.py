

# A = rock
# B = paper
# C = scissors

A = 1
B = 2
C = 3

t = {'X': 'A', 'Y': 'B', 'Z': 'C'}

d = {'A': 1, 'B':2, 'C': 3}

win = {'A': 'B', 'B': 'C', 'C': 'A'} # ex dom gissar A, vi gissar B
lose = {'A': 'C', 'B': 'A', 'C': 'B'}

score = 0

'''
# Part 1
with open('Day 2/Day2.txt') as f:
    for line in f:
        l = line.strip()
        if l != "":
            if l[0] == t[l[2]]: # If draw
                score += 3 + d[l[0]]
            elif l[0] == 'A' and t[l[2]] == 'C': # vi gissar C, dom A, vi förlorar
                score += d[t[l[2]]]
            elif l[0] == 'A' and t[l[2]] == 'B': # vi gissar B, dom A, vi vinner
                score  += d[t[l[2]]] +  6
            elif l[0] == 'B' and t[l[2]] == 'A': # vi gissar A, dom B, vi förlorar
                score += d[t[l[2]]] 
            elif l[0] == 'B' and t[l[2]] == 'C': # vi gissar C, dom B, vi vinner
                score += d[t[l[2]]] + 6
            elif l[0] == 'C' and t[l[2]] == 'B': # vi gissar B, dom C, vi förlorar
                score += d[t[l[2]]]
            elif l[0] == 'C' and t[l[2]] == 'A': # vi gissar A, dom C, vi vinner
                score += d[t[l[2]]] + 6
            else:
                score += 0
                print('fel')

print(score)
'''
# x = lose
# y = draw
# z = win


with open('Day 2/Day2.txt') as f:
    for line in f:
        l = line.strip()
        if l != "":
            if l[2] == 'X': # förlorar
                score += d[lose[l[0]]]
            elif l[2] == 'Y':
                score += 3 + d[l[0]]
            elif l[2] == 'Z':
                score += 6 + d[win[l[0]]]
            else:
                score += 0
                print('fel')

print(score)
