import scrapy
import csv


class BooksScrapeSpider(scrapy.Spider):
    name = "books_scrape"
    with open('book_data.csv','w') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Rating(Stars/5)', 'Link'])
        

    def start_requests(self):
        url = "https://books.toscrape.com/catalogue/page-{}.html"
        for p in range(1,51):
            yield scrapy.Request(url.format(p))


    def parse(self, response):        
        for page in response.xpath("//ol[@class='row']/li"):

            title = page.xpath("./article/h3/a/@title").get()
            price = page.xpath("./article/div/p[@class='price_color']/text()").get()
            rating = page.xpath("./article/p/@class").get()
            link = page.xpath("./article/h3/a/@href").get()

            
            with open('book_data.csv','a',newline='') as file:
                writer = csv.writer(file)
                writer.writerow([title, price, rating.split()[-1], link])