import requests, csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_books_from_page(page_url):
    """
    Downloads and parses a single page of books.

    Args:
        page_url (str): URL of the book page.

    Returns:
        tuple: (list of <article> elements containing books, BeautifulSoup object of the page)
    """
    response = requests.get(page_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    return books, soup


def clean_price(raw_price):
    """
    Cleans the price by removing symbols and unwanted characters.

    Args:
        raw_price (str): Raw price extracted from the HTML (e.g., '£51.77').

    Returns:
        str: Cleaned price (e.g., '51.77').
    """
    return raw_price.replace("£", "").replace("Â", "").strip()


def get_book_url(base_url, relative_link):
    """
    Builds the absolute URL of a book.

    Args:
        base_url (str): URL of the current page.
        relative_link (str): Relative link of the book.

    Returns:
        str: Absolute URL of the book.
    """
    return urljoin(base_url, relative_link)

def write_csv_header(output_file):
    """Creates CSV file and writes the header."""
    f = open(output_file, "w", newline="", encoding="utf-8-sig")
    writer = csv.writer(f)
    writer.writerow(["Title", "Price", "URL"])
    return f, writer

def write_book(writer, book, page_url):
    """Extracts book info and writes it to CSV."""
    title = book.h3.a["title"]
    raw_price = book.find("p", class_="price_color").text
    price = clean_price(raw_price)
    relative_link = book.h3.a["href"]
    book_url = get_book_url(page_url, relative_link)
    writer.writerow([title, price, book_url])


def scrape_page(writer, page_url):
    """Scrapes a single page and writes all books to CSV."""
    books, soup = get_books_from_page(page_url)
    for book in books:
        write_book(writer, book, page_url)
    # Returns the URL of next page if exists, else None
    next_button = soup.find("li", class_="next")
    if next_button:
        relative_link = next_button.a["href"]
        return get_book_url(page_url, relative_link)
    return None