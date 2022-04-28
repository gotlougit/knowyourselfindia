import random 

f = open("india")
articles = f.readlines()
l = len(articles)

def getArticle():
    return articles[random.randint(0,l)][:-1]
