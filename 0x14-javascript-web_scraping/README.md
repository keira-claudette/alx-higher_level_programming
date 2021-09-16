# JavaScript - Web scraping

##### Installations

You'll need to install:

- ###### Node 10

```
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

- ###### Semi-standard
[Documentation](https://github.com/standard/semistandard)

```
sudo npm install semistandard --global
```

- ###### Install `request` module
[Documentation](https://github.com/request/request)

```
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

###### Note: Request module has been deprecated since February 2020.
The team is considering an alternative to replace this module. It is, however really simple and powerful a module for practicing web-scraping in JavaScript.

### Concepts
- ###### [Node.js as a File Server](https://www.w3schools.com/nodejs/nodejs_filesystem.asp)

- ###### [The request module: Simplified HTTP client](https://github.com/request/request)

- ###### [Parsing JSON in js](https://www.google.com/search?q=reading+json+in+javascript&oq=reading+json+i&aqs=chrome.1.69i57j0i20i263i512j0i512l2j0i20i263i512j0i512l5.6718j0j7&sourceid=chrome&ie=UTF-8)

# Files
- `0-readme.js`: 
Reads and prints the content of a file.

- `1-writeme.js`: 
Writes a string to a file.

- `2-statuscode.js`: 
Displays the status code of a GET request.

- `3-starwars_title.js`:
Prints the title of a Star Wars movie where the episode number matches a given integer.

- `4-starwars_count.js`:
Prints the number of movies where the character “Wedge Antilles” is present.

- `5-request_store.js`:
Gets the contents of a webpage and stores it in a file.

- `6-completed_tasks.js`: 
Computes the number of tasks completed by user id.
