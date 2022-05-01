import json, pycurl, certifi
from io import BytesIO

scurl = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmnamespace=14&cmlimit=100&cmtitle="
pageurl = "https://en.wikipedia.org/w/api.php?action=query&format=json&list=categorymembers&cmtitle="

def processResponse(buffer):

    body = buffer.getvalue()
    body = body.decode("iso-8859-1")
    # Had to process JSON manually due to some formatting errors
    """
    body = json.loads(body)
    body = body["query"]["categorymembers"]
    
    titles = []
    for i in body:
        titles.append(i["title"])
    return titles
    """
    titles = []
    body = body.split("}")
    for i in body:
        if "title" in i:
            titles.append(i.partition("title")[-1][3:-1])
    return titles


def getSubCategory(pagename):

    buffer = BytesIO()
    c = pycurl.Curl()

    subcats = []

    if "Category:" in pagename:

        c.setopt(c.URL, scurl + pagename)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        c.perform()
        
        subcats += processResponse(buffer)
             
    c.setopt(c.URL, pageurl + pagename)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.perform()
    
    subcats += processResponse(buffer)

    c.close()

    return subcats
   
def crawlPages(pagename):

    subcats = getSubCategory(pagename.replace(" ","_"))
    normalpages = []
    othersubcats = []

    for i in subcats:
        print(i)
        if i.startswith("Category:"):
            i = i.replace(" ","_")
            x, y = crawlPages(i)
            othersubcats += x
            normalpages += y
        else:
            normalpages.append(i)
    
    with open("database.json","a") as f:
        json.dump(normalpages,f)
    return othersubcats, normalpages

pagename = "Category:India"
subcats, normalpages = crawlPages(pagename)

with open("database.json","w") as f:
    json.dump(normalpages, f)
