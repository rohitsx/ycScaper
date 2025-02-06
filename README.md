# ycScaper 

A Python-based tool to scrape Y Combinator company data, including startup URLs and social media links. 

## Installation 
Clone the repository:

```bash
git clone https://github.com/yourusername/ycScaper.git
cd ycScaper
```

Install dependencies:

```bash
sudo python -m venv /venv
pip install -r requirements.txt
```

## Usage Guide 

### 1. Obtain HTML Data
1. Visit [Y Combinator Companies](https://www.ycombinator.com/companies)
2. Scroll to the bottom to load all companies (automatic pagination)
3. Save the complete page as `companies.html`:
   - Right-click → **Save As**
   - Choose **Web Page, Complete** format
4. Move the saved file to the `html/` directory

### 2. Extract Startup URLs
Edit `getStartupUrl.py`:

```python
# Line 7 - Update path to your HTML file
your_downloaded_html = "html/companies.html"  #  Modify this path
```

Run the URL extractor:

```bash
python getStartupUrl.py
```

**Output:** `startupCsv/startup_urls.csv`

### 3. Scrape Social Media Links
Edit `getSocial.py`:

```python
# Line 7 - Update path to your URL CSV
your_new_create_url_csv = "startupCsv/startup_urls.csv"  # Modify this path
```

Run the social media scraper:

```bash
python getSocial.py
```

**Output:** JSON files in `socialJson/` directory

## Project Structure 

```
ycScaper/
├── getSocial.py          # Social media scraper
├── getStartupUrl.py      # URL extraction script
├── helper/               # Utility functions
├── html/                 # Store downloaded HTML files
├── socialJson/           # Social media data (JSON)
├── startupCsv/           # Startup URL lists (CSV)
├── requirements.txt      # Dependencies
└── venv/                 # Virtual environment (ignored)
```

## Example Outputs 

### `startup_urls.csv`

```csv
https://www.ycombinator.com/companies/abc-startup
https://www.ycombinator.com/companies/xyz-ventures
...
```

### `socialJson/abc-startup.json`

```json
{
  "name": "ABC Startup",
  "github": "https://github.com/abc",
  "twitter": "https://twitter.com/abc",
  "linkedin": "https://linkedin.com/company/abc"
  "x": "https://x.com/abc",
}
```

## Troubleshooting 
- **Missing HTML elements**: Ensure you saved the complete page after scrolling to load all companies
- **Empty CSV/JSON**: Check your file paths in the Python scripts
- **Connection errors**: Add delays between requests to avoid rate limiting


## Keywords for SEO 
Y Combinator Scraper Startup Data Extraction Web Scraping Tool Python Scraping Script YC Company Data Social Media Scraper Startup URL Extractor BeautifulSoup Scraping Data Mining Tool Y Combinator API Alternative Startup Research Tool Web Crawler for YC JSON and CSV Exporter  Python Data Scraping Y Combinator Analytics
