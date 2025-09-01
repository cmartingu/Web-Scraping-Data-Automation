from utils import get_books_from_page, write_csv_header, scrape_page
import traceback
import logging
import os

# Create data folder
os.makedirs("data", exist_ok=True)

# logging configuration, for .log file
logging.basicConfig(
    filename='data/scraper.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

BASE_URL = "https://books.toscrape.com/"

def scrape_all_books(output_file="data/results.csv"):
    """Iterates through all pages and saves results to CSV."""
    try:
        logging.info("Starting full web scraping...")
        f, writer = write_csv_header(output_file)
        next_page = BASE_URL
        total_books = 0

        while next_page:
            logging.info(f"Scraping {next_page}")
            books_count = sum(1 for _ in get_books_from_page(next_page)[0])
            total_books += books_count
            next_page = scrape_page(writer, next_page)

        f.close()
        logging.info(f"Finished scraping {total_books} books")

    except Exception as e:
        logging.critical(f"Fatal error: {e}")
        traceback.print_exc()
    finally:
        logging.info("End of web scraper")

if __name__ == "__main__":
    scrape_all_books()
