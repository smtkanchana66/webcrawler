# Simple Python Web Crawler

## Overview

This project is a **basic web crawler implemented in Python**.
It fetches web pages using the `urllib` library, extracts URLs using **regular expressions**, and **stores all discovered links in a text file**.

The crawler is designed for **learning purposes**, demonstrating how web pages can be fetched, parsed, and analyzed at a fundamental level without external frameworks.

---

## Features

* Fetches web pages using `urllib.request`
* Extracts URLs using Python `re` (regular expressions)
* Handles HTTP responses and errors
* Writes all discovered URLs to a `.txt` file
* Supports repeated crawling without overwriting previous results
* Works with local servers and public websites

---

## Technologies Used

* **Python 3**
* **urllib** – for HTTP requests
* **re (Regular Expressions)** – for URL extraction
* **Text file output** – for storing crawled URLs

---

## Project Structure

```
webcrawler/
│
├── webcrawler.py
├── urls.txt
└── README.md
```

* `webcrawler.py` – Main crawler script
* `urls.txt` – Output file containing all discovered URLs
* `README.md` – Project documentation

---

## How It Works

1. The crawler opens a starting URL using `urllib.request.urlopen()`
2. HTML content is read and decoded
3. Regular expressions are used to find all links (`href="..."`)
4. Each extracted URL is:

   * Printed (optional)
   * Appended to a text file
5. The crawler continues processing discovered links based on logic defined in the script

---

## Example Code Snippet

```python
import urllib.request, urllib.parse, urllib.error
import re 
url_lst = list()
temp_url = 'https://www.example.com'

while True:
    #fhand = urllib.request.urlopen(temp_url)
    #print("This is temp url",temp_url,len(url_lst))

    try:
        fhand = urllib.request.urlopen(temp_url)
    except urllib.error.HTTPError as e:
        print("HTTP error:", e.code, temp_url)
    except urllib.error.URLError as e:
        print("URL error:", e.reason, temp_url)
    

    for line in fhand:
        decoded_line = line.decode('utf-8', errors='ignore').strip()
        url = re.findall('"(http[s]?://\\S+)"', decoded_line)
        #print("URL FINDED", url)
```

---

## Output

All discovered URLs are saved in:

```
Url_list.txt
```

Each URL is written on a new line.
The file uses **append mode**, so previously saved URLs are preserved.

---

## How to Run

1. Ensure Python 3 is installed
2. Navigate to the project directory
3. Run the crawler:

```bash
python3 webcrawler.py
```

4. View extracted URLs in `Url_list.txt`

---

## Learning Objectives

* Understand how web crawling works at a low level
* Learn how HTTP requests are made in Python
* Practice using regular expressions on real HTML
* Handle file writing correctly inside loops
* Understand common crawler errors such as HTTP 404

---

## Disclaimer

This crawler is intended for **educational purposes only**.
Always respect website rules `robots.txt` and terms of service when crawling public websites.

---
