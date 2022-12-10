


with open('Day 10/day10.txt') as f:

    data = f.readlines()

    t_0 = 0
    t_1 = 1
    t_2 = 0
    x = 1
    sum = 0
    clock = 1

    def check(i, sum, x):
        if (i+20) % 40 == 0 and i < 221:
            sum += i * x
        return sum

    for d in data:
        line = d.strip().split()
        command = line[0]

        if command == "addx":
            num = int(line[1])
            clock += 1
            sum = check(clock, sum, x)
            clock += 1
            x += num
            sum = check(clock, sum, x)
        else:
            clock += 1
            sum = check(clock, sum, x)

print(sum)



