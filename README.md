# Know Yourself, India

## Overview

As a part of Hackshetra 2022, we were given several prompts to build programs on. I had chosen the following:

"India, a country full of diversity and cultures, have so many languages, food, clothes and traditions. Every place and culture have its own beauty. Suggest some ideas how can we experience them in any way."

My solution was to create a small website which loads in a random fun fact or trivia piece about a particular place in India. It would display some pictures and facts, and perhaps even a map with the location marked on it. This would serve as a nice way of reminding people of the diversity of India and encourage us to appreciate “unity in diversity” enshrined in our Constitution.

## Design

The backend will have two components: a crawler and a web server.

The crawler will (as is evident) crawl Wikipedia for India-related pages. The output of the Wikipedia API is then processed to remove useless sections (for our purposes, anyway), like References, and those [edit]() URLs too. The links are all relative to Wikipedia as well, which is also something that gets fixed.

The crawler just dumps its output to a text file for now, but it will eventually be stored in a database, which will allow easier querying and faster handling of huge amounts of pages.

The web server (run using Flask) will then fetch a random page and display it to the user, along with some stylish CSS to jazz the page up! This is the least developed part of the website for now, as the output of the API needs to be processed completely. Many pages and sections will most likely be removed due to them being irrelevant.

Not much processing will be done client-side for now.

## Acknowledgements

Thanks to the Hackshetra 2022 organizers for holding such an event; it was certainly an amazing experience, and I look forward to the next session

Thanks especially to Wikipedia for being such an open and useful source of information to all. The amount of metadata and API access they offer is simply mind-boggling.

## TODO

- Migrate the list of articles to a proper database for easy removal, querying and filtering and cache all this info so we don't end up wasting Wikipedia's bandwidth

- Use POST to send reports against certain articles instead of GET

- Make the website look good

- Add proper code to update database periodically to get more up to date info, and crawl more URLs as well
