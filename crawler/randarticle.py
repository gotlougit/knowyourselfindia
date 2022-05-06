import random

with open("tables.json") as f:

    x = f.readlines()
    l = len(x)
    i = random.randint(0,l)
    print(x[i])
