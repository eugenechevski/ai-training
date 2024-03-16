import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def scrape_articles(URL):
    # Initialize a Chrome driver (you can choose other browsers like Firefox or PhantomJS if needed)
    driver = webdriver.Chrome()

    # Navigate to the URL
    driver.get(URL)

    # Wait for the dynamic content to load (you may need to adjust the time based on how long it takes to load)
    driver.implicitly_wait(3000)

    # Now, get the HTML using BeautifulSoup from the rendered page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Rest of the code remains the same
    titles = []
    urls = []

    for article in soup.find_all('h2'):
        title = article.text.strip()
        titles.append(title)

    for link in soup.find_all('a', href=True):
        url = link['href']
        urls.append(url)

    driver.quit()  # Close the browser after scraping

    return titles, urls

# Replace `URL` with the actual URL of the news website's homepage
URL = "https://www.eugenechevski.com/"

titles, urls = scrape_articles(URL)

# Print the extracted data
for title, url in zip(titles, urls):
    print(f"Title: {title} - URL: {url}")