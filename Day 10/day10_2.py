with open('Day 10/day10.txt') as f:

    data = f.readlines()

    image = []
    x = 1
    clock = 0

    def check(i, x, list):
        if (i % 40) == x-1 or (i % 40) == x or (i % 40) == x+1:
            list.append('#')
        else:
            list.append(' ')
        return list

    for d in data:
        line = d.strip().split()
        command = line[0]

        if command == "addx":
            num = int(line[1])     
            image = check(clock, x, image)
            clock += 1 
            image = check(clock, x, image)
            x += num
            clock += 1
        else: 
            image = check(clock, x, image)
            clock += 1

print(len(image))
print(''.join(image[:40]))
print(''.join(image[40:80]))
print(''.join(image[80:120]))
print(''.join(image[120:160]))
print(''.join(image[160:200]))
print(''.join(image[200:240]))


# EZFPRAKL


