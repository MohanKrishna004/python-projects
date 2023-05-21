import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url):
    response = requests.get(url)

    
    if response.status_code == 200:
    
        soup = BeautifulSoup(response.content, 'html.parser')
        product_titles = soup.find_all('h2', class_='product-title')
        product_prices = soup.find_all('span', class_='product-price')
        with open('scraped_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Price'])
            for title, price in zip(product_titles, product_prices):
                writer.writerow([title.text.strip(), price.text.strip()])

        print("Scraping complete. Data saved to 'scraped_data.csv'.")
    else:
        print("Error accessing the website.")

website_url = "https://www.example.com/products"

scrape_website(website_url)
