

'''
        [G]         [D]     [Q]    
[P]     [T]         [L] [M] [Z]    
[Z] [Z] [C]         [Z] [G] [W]    
[M] [B] [F]         [P] [C] [H] [N]
[T] [S] [R]     [H] [W] [R] [L] [W]
[R] [T] [Q] [Z] [R] [S] [Z] [F] [P]
[C] [N] [H] [R] [N] [H] [D] [J] [Q]
[N] [D] [M] [G] [Z] [F] [W] [S] [S]
 1   2   3   4   5   6   7   8   9 

'''


l1 = ['N', 'C', 'R', 'T','M', 'Z', 'P']
l2 = ['D', 'N', 'T', 'S', 'B', 'Z']
l3 = ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G']
l4 = ['G', 'R', 'Z']
l5 = ['Z', 'N', 'R', 'H']
l6 = ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D']
l7 = ['W', 'D', 'Z', 'R', 'C', 'G', 'M']
l8 = ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q']
l9 = ['S', 'Q', 'P', 'W', 'N']

ll = [l1, l2, l3, l4, l5, l6, l7, l8, l9]



'''
l1 = ['Z', 'N']
l2 = ['M', 'C', 'D']
l3 = ['P']

ll = [l1, l2, l3]
'''




'''
with open('Day 5/day5.txt') as f:
    for i in f:
        t = i.strip().split(' ')
        for nr_moves in range(int(t[1])):
            ll[int(t[5])-1].append(ll[int(t[3])-1].pop())

out = ''
for i in ll:
    print(i)
    print(i[-3:])
    out += i[-1]
print(out)


'''
for i in ll:
    print(i)
print()

with open('Day 5/day5.txt') as f:
    for i in f:
        t = i.strip().split(' ')
        print(t)

        nr_moves = int(t[1])
        #print(nr_moves)
        #print(ll[int(t[5])-1])
        #print(ll[int(t[5])-1][-nr_moves:])
        temp = ll[int(t[3])-1][-nr_moves:].copy()
        #temp.reverse()
        # ll[int(t[5])-1] = ll[int(t[5])-1] + ll[int(t[3])-1][-nr_moves:].reverse()
        ll[int(t[5])-1] = ll[int(t[5])-1] + temp
        ll[int(t[3])-1] = ll[int(t[3])-1][:-nr_moves or None]

        for i in ll:
            print(i)
        print()
        



        #ll[int(t[5])-1].append()
        #print(ll[int(t[3])-1][-nr_moves:])
        #ll[int(t[5])-1].append()
        #ll[int(t[3])-1]
        #l#st = lst[:-n or None]


out = ''
for i in ll:
    print(i)
    out += i[-1]
print(out)


