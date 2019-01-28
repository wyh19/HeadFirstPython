"""练习写入文件"""

man = []
other = []

try:
    data = open('./sketch.txt')
    for line in data:
        try:
            (role, spoken) = line.split(':', 1)
            spoken = spoken.strip()
            if role == 'Man':
                man.append(spoken)
            elif role == 'Other Man':
                other.append(spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

print(man)
print(other)

#开始写入文件
out  = open('./data.out','w')
print(man,file = out)
print(other,file = out)
out.close()