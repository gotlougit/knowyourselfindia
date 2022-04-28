# Know Yourself, India

## Overview

As a part of Hackshetra 2022, we were given several prompts to build programs on. I had chosen the following:

"India, a country full of diversity and cultures, have so many languages, food, clothes and traditions. Every place and culture have its own beauty. Suggest some ideas how can we experience them in any way."

My solution was to create a small website which loads in a random fun fact or trivia piece about a particular place in India. It would display some pictures and facts, and perhaps even a map with the location marked on it. This would serve as a nice way of reminding people of the diversity of India and encourage us to appreciate “unity in diversity” enshrined in our Constitution.

The backend is being done in Python with Flask, and the frontend is just some very basic HTML, CSS, and JavaScript. Right now, it has a list of all the articles in English Wikipedia with "India" in them or some variation of it in a text file (which will eventually be stored in a database of some kind, either SQLite or Postgres).

When a user loads the website, the backend simply selects a random article title from the list and serves a webpage which has instructions to fetch an extract of that article from Wikipedia. For simplicity's sake this is being done because the list of articles needs to be further filtered out to get more relevant and fun facts rather than some random article about, say, the Native Americans.

In the final build, the extracts will likely be cached as by that point of time, there will be so little articles the cost of doing so is fairly low. This also helps avoid Wikipedia rate limiting users, and gives more control to us to control resource usage and improve user experience.

Note: the dump I used to obtain all the Wikipedia articles can be found [here](https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz)

## Acknowledgements

Thanks to the Hackshetra 2022 organizers for holding such an event; it was certainly an amazing experience, and I look forward to the next session

Thanks especially to Wikipedia for being such an open and useful source of information to all. The amount of metadata and API access they offer is simply mind-boggling.

## TODO

- Migrate the list of articles to a proper database for easy removal, querying and filtering

- Clean up JavaScript code; it's just embedded in the HTML page for now

- Use POST to send reports against certain articles instead of GET

- Make the website look good

- Fetch images for certain articles

- Cache all this info so we don't end up wasting Wikipedia's bandwidth
