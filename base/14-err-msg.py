try:
    data = open('missing.txt')
    print(data.readline())
except IOError as err:
    print('FileError:'+str(err))
finally:
    if 'data' in locals():
        data.close()

