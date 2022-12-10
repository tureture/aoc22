import numpy as np

def move(t, h, prev_h):

    if (max(abs(h - t)) > 1):
        t = prev_h.copy()

    return t




visited = [(0,0)]
t = np.array([0, 0])
h = np.array([0, 0])
prev_h = np.array([0, 0])

with open('Day 9/day9.txt') as f:

    data = f.readlines()

    for line in data:
        line = line.strip().split()
        direction = line[0]
        steps = int(line[1])

        if direction == 'U':
            for i in range(steps):
                prev_h = h.copy()
                h[1] += 1
                visited.append((t[0], t[1]))
                t = move(t, h, prev_h)
                


        elif direction == 'D':
            for i in range(steps):
                prev_h = h.copy()
                h[1] -= 1    
                visited.append((t[0], t[1]))  
                t = move(t, h, prev_h)
                            

        elif direction == 'L':
            for i in range(steps):
                prev_h = h.copy()
                h[0] -= 1
                visited.append((t[0], t[1]))
                t = move(t, h, prev_h)
                
                

        elif direction == 'R':
            for i in range(steps):
                prev_h = h.copy()
                h[0] += 1
                visited.append((t[0], t[1]))
                t = move(t, h, prev_h)

                
        else:
            print('fel')
        
#print(visited)
# print(set(visited))
print(len(set(visited)))




        


