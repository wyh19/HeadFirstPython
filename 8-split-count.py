
data = open('./sketch.txt')

for line in data:
    (role, spoken) = line.split(':',1)
    print(role+' said:', end='')
    print(spoken, end='')

data.close()

#将line.split(':') 替换为 line.split(':',1)，确实解决了一行中多个：时的问题，但是没有：的一行又有问题了