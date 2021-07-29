import os

def mkfiles(path,filename):
    for i in range(0,9):
        with open(path + filename + '_' + str(i), "w") as f:
            f.write('some text data ' + str(i))

def checknmake(homedir):
    shared = homedir + '/shared/'
    if not os.path.isdir(shared):
        print('Folder - 404. Make folder \'shared/\'')
        os.mkdir(shared)
    return shared
    
