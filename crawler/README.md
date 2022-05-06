# Know Yourself India Crawler

## How to Use

1. Run crawler.py. This generates a list of all the list names that are associated with India. It does this by recursively requesting all the lists and subcategories inside the page "Category:India" and then does the same thing to all subcategories within that page and so on and so forth.

The output of crawler.py is saved within ```database.json```.

2. Run loader.py.

This script downloads all the mentioned pages in ```database.json``` in sections, so that we can easily isolate and remove useless sections as well as get the critical information, like the tables or lists easily.

Note: this program tends to crash and it has almost never gotten all the URLs saved. 

The output of loader.py is saved in ```tables.json```, so named because primarily we want tables with information saved here.

3. Run cleanse.py

This script just goes through every record saved inside ```table.json``` and cleans it up.

Right now, it just fixes certain links so they point correctly to Wikipedia.

### WARNING:
It DOES NOT SAVE ITS OUTPUT ANYWHERE, it just prints it to STDOUT

Save it wherever you want, preferably in server/ so that Flask knows where to request it.

## On randarticle.py

This is just a convenient way to test before deploying. Simply redirect it's output to a file and open it in your browser of choice to view a random entry.
