import re

with open('upcoming.csv','r') as f:
    with open('format.csv','w') as g:
        for line in f.readlines():
            text = line.replace("['","").replace("']","")
            g.write(text)

