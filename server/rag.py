import random

with open("tables.json") as f:
    articles = f.readlines()

    l = len(articles)

def getArticle():
    x = articles[random.randint(0,l)][:-1]
    print(x)
    return x
