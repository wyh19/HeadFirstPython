
data = open('./file/sketch.txt')

for line in data:
    if line.find(':') > -1:
        (role, spoken) = line.split(':', 1)
        print(role+' said:', end='')
        print(spoken, end='')

data.close()

# if line.find(':') > -1:  可以写成  if not line.find(':') == -1
