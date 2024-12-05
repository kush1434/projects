# Books Scrape Project

## Overview

This Python project uses the Scrapy framework to scrape data from the "Books to Scrape" website. The script extracts book titles, prices, ratings, and links to individual book pages, saving the information into a CSV file for easy access and analysis.

## Features

- Scrapes book titles, prices, ratings (in stars), and links.
- Iterates through all 50 pages of the website catalog.
- Saves the extracted data in a CSV file named `book_data.csv`.
- Provides well-structured and clean output for analysis.

## Installation

1. Install Python 3.9 or higher.
2. Install the Scrapy library using pip:
   pip install scrapy

## Usage

1. Save the script as books_scrape.py.
2. Run the script from the terminal:
    scrapy runspider books_scrape.py
3. After completion, the scraped data will be available in the book_data.csv file.

## Output Format

- Title: The title of the book.
- Price: The price of the book (e.g., £51.77).
- Rating (Stars/5): The star rating of the book (e.g., 3 for a 3-star rating).
- Link: The relative link to the book's detail page.