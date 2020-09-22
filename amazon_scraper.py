from bs4 import BeautifulSoup
from requests_html import HTMLSession
import requests

class Scraper:
    
    def __init__(self,url,budget):
        self.url = url
        self.budget = budget
        self.session = HTMLSession()
        self.webpage = self.session.get(self.url).content
        self.parser = 'lxml'
        self.soup = BeautifulSoup(self.webpage,self.parser)

    def __str__(self):
        return self.soup.prettify()

    def get_title(self):
        self.product_title = self.soup.find('span',id='productTitle').text.strip()
        print(self.product_title)
    
    def get_price(self):
        price_raw = self.soup.find('span',id='priceblock_ourprice').text.strip()
        price_filtered = price_raw[2:len(price_raw)-3]
        self.product_price = int(''.join([x for x in price_filtered if x is not ',']))
        print(self.product_price)
        return


def main():
    url = input("Paste the link of the Amazon product whose price you wish to monitor:")
    budget = int(input("Enter you budget price:"))
    c3po = Scraper(url,budget)
    c3po.get_price()
    #print(c3po)

if __name__ == '__main__':
    main()