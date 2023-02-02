import os

for file in os.listdir('folder'):
    with open(os.path.join('folder', file), 'r', encoding= 'utf-8') as f:
        a = f.readlines()
        counter = 0
        c = {}
        #b = len(sorted(a))
        #print(b)
        for i in a:
            counter += 1
            c = {counter: a}
        for k in range():
            print(k)

