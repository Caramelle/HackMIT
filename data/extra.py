from imdb import *

with open('format.csv','r') as f:
    with open('extras.csv','w') as g:
        for line in f.readlines()[1:]:
            title = line.split(',')[0]
            extras=''
            try:
                extras=getExtra(title)
                line=line.replace('\r\n','')
                line+=','+str(extras)+'\r\n'
                g.write(line)
                print line
            except:
                pass
