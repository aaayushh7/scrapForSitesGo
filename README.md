

```
# Web Scraping Project: Stanford Neurology Faculty Data

## Project Overview

This project involves scraping data from the Stanford Neurology Faculty webpage and organizing it in a Google Sheets document. The data includes faculty names, individual profile links, and email addresses.

## Source Website

The data is scraped from the following URL: 'https://med.stanford.edu/neurology/faculty/overview.html?tab=proxy'

## Data

The following data is collected from the website:

- **Names**: The names of the faculty members are scraped from the main page.
- **Profile Links**: The individual profile links of the faculty members are collected from the href attribute of their names on the main page.
- **Emails**: The email addresses of the faculty members are collected from their individual profile pages.

## Tools and Libraries Used

- **Web Scraping**: Python's BeautifulSoup library is used for web scraping.
- **Data Storage**: The `gspread` library and Google Sheets API are used to store and organize the data in a Google Sheets document.

## How to Run the Project

1. Clone the GitHub repository.
2. Install the necessary Python libraries (BeautifulSoup, gspread).
3. Run the Python script to start the web scraping process.
4. Check the Google Sheets document for the scraped and organized data.

## Note

Please ensure you have the necessary permissions to scrape data from the website and use the data responsibly.

```
