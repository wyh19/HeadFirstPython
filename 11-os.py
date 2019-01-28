from os.path import exists

file_path = './sketch.txt'

if exists(file_path):
    data = open(file_path)
    for line in data:
        if not line.find(':') == -1:
            (role, spoken) = line.split(':', 1)
            print(role+'said:', end='')
            print(spoken, end='')
    data.close()
else:
    print('The Data file is missing')

# 尝试将file_path的值改成别的