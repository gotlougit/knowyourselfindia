import json, pycurl, certifi
from io import BytesIO

l = []

with open("database.json") as f:
    
    lines = f.readlines()
    for i in lines:
        if i != "\n":
            x = json.loads(i)
            for j in x:
                if j not in l:
                    l.append(j)

url1 = "https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=sections&page="
url2 = "https://en.wikipedia.org/w/api.php?action=parse&prop=text&format=json&section="
url_part = "&page="

data = []

for i in l:
    
    buffer = BytesIO()
    c = pycurl.Curl()

    c.setopt(c.URL, url1 + i.replace(" ","_"))
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    try:
        c.perform()
    except:
        break;

    body = buffer.getvalue()
    body = body.decode("iso-8859-1")
    
    body = (json.loads(body))
    body = (body["parse"]["sections"])

    for j in body[1:]:
        
        buffer = BytesIO()
        c.setopt(c.URL, url2 + j["index"] + url_part + i.replace(" ","_"))
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        try:
            c.perform()
        except:
            break;
        
        b = buffer.getvalue()
        b = b.decode("iso-8859-1")
        b = json.loads(b)["parse"]["text"]["*"]
        data.append(b)
        with open("table.json","a") as f:
            json.dump(b, f)
            f.write("\n")

with open("tables.json","w") as f:
    json.dump(data, f)
