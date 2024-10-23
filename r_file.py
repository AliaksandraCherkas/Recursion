import os
path = 'c:\\Users\\User\\Desktop\\Docker'
# print(os.listdir(path))

def round_file(path, level = 1):
    print(f'level = {level}, content = {os.listdir(path)}')
    for i in os.listdir(path):
        # print(i, type(i), path + '\\' + i, os.path.isdir(path + '\\' + i))
        if os.path.isdir(path + '\\' + i):
            round_file(path + '\\' + i, level+1)
        
round_file(path)