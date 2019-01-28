
data = open('./sketch.txt')

for line in data:
    try:
        (role, spoken) = line.split(':', 1)
        print(role+' said:', end='')
        print(spoken, end='')
    except:
        pass

data.close()
