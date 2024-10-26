from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
import time

# Specify the path to geckodriver if it's not in your system's PATH
gecko_path = './geckodriver'  # Replace with your actual geckodriver path

# Set up the Firefox WebDriver service
service = Service(executable_path=gecko_path)

# Set up the Firefox WebDriver
driver = webdriver.Firefox(service=service)

# Function to scrape webpage
def scrape_with_firefox(url):
    # Open the website
    driver.get(url)

    # Optional: Wait for the page to load (especially useful for pages with dynamic content)
    time.sleep(2)

    # Get the page source and parse it with BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')  # Corrected parser name
    
    # Example 1: Print the page title
    print(f"Page Title: {soup.title.string}")

    # Example 2: Print all links on the page
    print("\nAll links on the Page:")
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.get_text(strip=True)
        if href:
            print(f"Text: {text}, URL: {href}")

# Run the scraper
try:
    scrape_with_firefox("https://example.com")
finally:
    # Close the browser after scraping
    driver.quit()
    print("Browser closed.")
