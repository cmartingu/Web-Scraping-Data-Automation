# Web-Scraping-Data-Automation

Este proyecto es un script en **Python** que realiza web scraping sobre la página [Books to Scrape](https://books.toscrape.com/) para extraer información sobre los libros disponibles.  
Los datos extraídos incluyen:  

- **Título del libro**  
- **URL directa al libro**  
- **Precio**  

Los resultados se guardan en un archivo **CSV** dentro de la carpeta `data/`.

---

## 🚀 Instalación

1. Clona este repositorio o descarga los archivos del proyecto.

```bash

git clone https://github.com/cmartingu/Web-Scraping-Data-Automation
```
2. Asegúrate de tener **Python 3** instalado.  
3. Instala las dependencias ejecutando:  

```bash

pip install -r requirements.txt
```

## 📂 Initial structure of the project
```bash

Web-Scraping-Data-Automation
├── src/
│   └── scraper.py        # Principal script
|   └── utils.py          # Utils to use
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## 🛠️ Use
Once you have cloned the repo, execute the next command
```bash

cd Web-Scraping-Data-Automation
python src/scraper.py
```
Esto recorrerá todas las páginas de Books to Scrape y guardará los resultados en data/results.csv.

## 📂 Final structure of the project
```bash

Web-Scraping-Data-Automation
├── data/
│   └── results.csv       # Results
|   └── scraper.log       # LOG file
├── src/
│   └── scraper.py        # Principal script
|   └── utils.py          # Utils to use
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

## 📑 Ejemplo de salida
El archivo results.csv tendrá un formato como el siguiente:
```csv

title,url,price
A Light in the Attic,51.77,https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
Tipping the Velvet,53.74,https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html
Soumission,50.10,https://books.toscrape.com/catalogue/soumission_998/index.html
...
```

