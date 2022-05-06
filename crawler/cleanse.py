import re

with open("table.json") as f:
    
    x = f.readlines()
    for i in x:
        i = i[1:-2]
        i = i.replace("\\n","")
        #regex substitution
        try:
            results = re.findall(r'href=\\"[A-Za-z0-9&?=_:;/]*\\"', i)
            for r in results:
                newr =  'href="https://en.wikipedia.org' + r[7:-2] + '"'
                i = i.replace(r, newr)
            print(i)
        except:
            continue
