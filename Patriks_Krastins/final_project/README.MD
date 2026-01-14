# Selenium Chrome Automation

This Python script uses **undetected-chromedriver** and **Selenium** to scrape 3 random article from Delfi.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Description

This script goes to https://www.delfi.lv/zinas grabs 3 random articles. Saves the link, title and then goes to each link and gets the article body.
All the info gets saved into text files

info.txt is for the title and link
text.txt is for the article body

After this further auotmations can be easily implemented, like calling a LLM api to summerize choosen articles etc. 