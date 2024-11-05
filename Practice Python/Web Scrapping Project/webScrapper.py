# Web Scraper: Scrape a website (e.g., IMDB or Wikipedia) to gather information like movie ratings, descriptions, or trending topics.

<<<<<<< HEAD

=======
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    """Fetch the content of the webpage."""
    response = requests.get(url)

    # Check if the request is successful
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None
    
def parse_page(html_content):
    """Parse the html content using BeautifulSoup"""
    soup =  BeautifulSoup(html_content, 'html.parser')

    # Example 1: Get the title of the page 
    page_title =  soup.title.string
    print(f"Page Title: {page_title}")

    # Example 2: Extract all links from the page
    links = soup.find_all('a')
    print("\n All Links on the Page: ")
    for link in links:
        href =  link.get('href')
        text = link.get_text(strip = True)
        if href:
            print(f"Text: {text}, URL: {href}")

def web_scrapper():
    # URL of the webpage you want to scrape
    url = input("Enter the URL of the website to scrape: ")

    # Step 1: Fetch the page content
    html_content =fetch_page(url)

    if html_content:
        # Step 2: Parse and extract information
        parse_page(html_content)

# Run the web scrapper
if __name__ == "__main__":
   web_scrapper()
>>>>>>> 68b523ece3ae9fc72d88979a82621eba402a7180
