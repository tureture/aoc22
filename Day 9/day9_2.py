

import numpy as np

def move(pos, head):

    if (max(abs(pos - head)) <= 1): # kolla om den ska flytta
        return pos
    else:
        # same row -> move col
        if (pos[0] == head[0]):
            if pos[1] > head[1]:
                pos[1] -= 1
            else:
                pos[1] += 1
        elif pos[1] == head[1]: # same col -> move row
            if pos[0] > head[0]:
                pos[0] -= 1
            else:
                pos[0] += 1
        else: # move diag
            pos[0] -= 1 * np.sign(pos[0] - head[0])
            pos[1] -= 1 * np.sign(pos[1] - head[1])

    return pos

visited = [(0,0)]
t = np.zeros((9,2), dtype=int)
prev_h = np.zeros((9,2), dtype=int)

h = np.array([0, 0])
# prev_h = np.array([0, 0])

with open('Day 9/day9.txt') as f:

    data = f.readlines()

    for line in data:
        line = line.strip().split()
        direction = line[0]
        steps = int(line[1])

        if direction == 'U':
            for i in range(steps):

                h[1] += 1
                t[0, :] = move(t[0, :], h)
                for k in range(1, len(t)):
                    t[k, :] = move(t[k, :], t[k-1, :])           
                visited.append((t[8, 0], t[8, 1]))
                
        elif direction == 'D':
            for i in range(steps):

                h[1] -= 1
                t[0, :] = move(t[0, :], h)
                for k in range(1, len(t)):
                    t[k, :] = move(t[k, :], t[k-1, :])           
                visited.append((t[8, 0], t[8, 1]))
                            
        elif direction == 'L':
            for i in range(steps):

                h[0] -= 1
                t[0, :] = move(t[0, :], h)
                for k in range(1, len(t)):
                    t[k, :] = move(t[k, :], t[k-1, :])           
                visited.append((t[8, 0], t[8, 1]))
                
        elif direction == 'R':
            for i in range(steps):
                
                h[0] += 1
                t[0, :] = move(t[0, :], h)
                for k in range(1, len(t)):
                    t[k, :] = move(t[k, :], t[k-1, :])           
                visited.append((t[8, 0], t[8, 1]))


               
        else:
            print('fel')



        
#print(visited)

# print(set(visited))
print(len(set(visited)))


