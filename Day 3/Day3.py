


score = 0


'''
with open('Day 3/day3.txt') as f:

    for line in f:
        l = line.strip()
        fhalf = l[:len(l)//2]
        lhalf = l[len(l)//2:]

        for c1 in fhalf:
            for c2 in lhalf:
                if c1 == c2:
                    temp = c1

        print(temp)
        if temp.isupper():
            score += ord(temp) - 38
        else:
            score += ord(temp) - 96

               
print(score)
print(ord('z') - 96)
print(ord('A') - 38)
'''

score = 0
with open('Day 3/day3.txt') as f:
    lines = f.readlines()
    for i in range(len(lines) // 3):
        print(i)
        l1 = lines[i*3].strip()
        l2 = lines[i*3+1].strip()
        l3 = lines[i*3+2].strip()

        done = False
        for c1 in l1:
            for c2 in l2:
                for c3 in l3:
                    if c1 == c2  and c1 == c3 and c2 == c3:
                        temp = c1

        if temp.isupper():
            score += ord(temp) - 38
        else:
            score += ord(temp) - 96

               
print(score)





        
