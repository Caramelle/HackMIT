from imdb import *

with open('format.csv','r') as f:
    with open('rated.csv','w') as g:
        for line in f.readlines()[1:]:
            title = line.split(',')[0]
            good = isGood(title)
            line=line.replace('\r\n','')
            line+=','+str(good)+'\r\n'
            g.write(line)
            print line
