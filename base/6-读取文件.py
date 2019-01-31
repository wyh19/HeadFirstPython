"""练习文件的处理"""

the_file = open('data-file/sketch.txt')

print(the_file.readline(),end='')
print(the_file.readline(),end='')

print('----以上只是练习-----')

the_file.seek(0)

for line in the_file:
    print(line,end='')

the_file.close()