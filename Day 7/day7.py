
folders = {'/':0}
active_folders = []
old_folders = []
a_folders = {}
current_folder = '/'
all_folders_debug = []
quickfix = {'/':0}


with open('Day 7/day7.txt') as f:
    data = f.readlines()
    for i in data:
        line = i.strip()
        if line == "$ ls":
            pass
        elif line == "$ cd ..":
            active_folders.pop()
        elif line[0:4] == "$ cd":
            active_folders.append(''.join(active_folders) + line[5:])
        elif line[0:3] == "dir":
            name = ''.join(active_folders) + line[4:]
            if name not in folders:
                folders[name] = 0
        else:
            temp = line.split(' ')
            for f in active_folders:
                folders[f] += int(temp[0])




print(''.join(active_folders))


sum = 0
n = 0
for key in folders:
    # print(key, folders[key])
    if folders[key] < 100000:
        n += 1
        sum += folders[key]


print(sum)


hej = {k: v for k, v in sorted(folders.items(), key=lambda item: item[1])}
for key in hej:
        if hej[key] >= 10216456:
            print(key, hej[key])
            break

print(70000000 - 50216456 - 30000000)
# 20216456
