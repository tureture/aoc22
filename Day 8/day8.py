import numpy as np

mh = 0
mv = 0
mu = 0
mn = 0

size = 99


with open('Day 8/day8.txt') as f:

    data = f.readlines()

    d = np.zeros([size,size], dtype=int)

    for i in range(len(data)):
        line = data[i].strip()
        for j in range(len(line)):
            d[i,j] = int(line[j])


counter = 0
edges = 0

'''
for i in range(size):
    for j in range(size):
    
        mh = max(d[i,j+1:], default=-1)
        mv = max(d[i,:j], default=-1)
        mn = max(d[i+1:, j], default=-1)
        mu = max(d[:i,j], default=-1)

        if mh < d[i,j] or mv < d[i,j] or mu < d[i,j] or mn < d[i,j]:
            counter += 1

'''
hc = 1
vc = 1
nc = 1
uc = 1

score = np.zeros([size, size], dtype=int)



for i in range(size):
    for j in range(size):

        h = d[i,j+1:-1]
        v = d[i,1:j]
        n = d[i+1:-1,j]
        u = d[1:i,j]


        for x in h:
            if x < d[i,j]:
                hc += 1
            else:
                break

        for x in np.flip(v):
            if x < d[i,j]:
                vc += 1
            else:
                break

        for x in n:
            if x < d[i,j]:
                nc += 1
            else:
                break

        for x in np.flip(u):
            if x < d[i,j]:
                uc += 1
            else:
                break
        
        '''
                print(d)
        print('val: ', d[i,j])
        print('index: ', i+1,j+1)
        print(hc, vc, nc, uc)
        print((hc * vc * nc * uc))
        print('------------------')
        
        '''

        

        score[i,j] = (hc * vc * nc * uc)

        hc, vc, nc, uc = 1,1,1,1
        

print(score)
print(max(score.flatten()))
print(counter)


