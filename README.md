# Web-Scraping-Data-Automation

This project is a **Python script** that performs web scraping on the [Books to Scrape](https://books.toscrape.com/) website to extract information about the available books.  
The extracted data includes:  

- **Book title**  
- **Price**  
- **Direct book URL**  

The results are saved in a **CSV file** inside the `data/` folder.

---

## 🚀 Installation

1. Clone this repository or download the project files:

```bash
git clone https://github.com/cmartingu/Web-Scraping-Data-Automation
```
2. Make sure to have **Python 3** installed.
3. Get into the directory cloned:
```bash
cd Web-Scraping-Data-Automation
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## 📂 Initial Project Structure
```bash
Web-Scraping-Data-Automation
├── src/
│   └── scraper.py        # Main script
|   └── utils.py          # Utility functions
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 🛠️ Usage
Execute the next command:
```bash
python src/scraper.py
```
The scraper will iterate through all pages of Books to Scrape and save the results into data/results.csv.

## 📂 Final structure of the project
```bash

Web-Scraping-Data-Automation
├── data/
│   └── results.csv       # Extracted results
|   └── scraper.log       # Log file
├── src/
│   └── scraper.py        # Main script
|   └── utils.py          # Utility functions
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 📑 Example Output
The results.csv file will look like this:
```csv

title,url,price
A Light in the Attic,51.77,https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
Tipping the Velvet,53.74,https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html
Soumission,50.10,https://books.toscrape.com/catalogue/soumission_998/index.html
...
```
