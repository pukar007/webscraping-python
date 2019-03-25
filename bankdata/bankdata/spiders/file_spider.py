import scrapy

from  ..items import BankdataItem

class filespider(scrapy.Spider):

    name = 'databot'
    start_urls = [
        'https://www.everestbankltd.com/supports/interest-and-rates/fees-and-services/'
                 ]
         # def get_urls(self,filename):
         #   f = open('list.txt').read().split()
         # urls=[]
         # for i in f:
         #     urls.append(i)
         #return urls
         #allowed_domains=["databot.org"]

            #f=open("list.txt")

           #f.close   //urlstart_urls=[strip() for url in f.readlines()]

                    #if filename :
            # with open ('list.txt' , 'r') as f:
            # self.start_urls =[url.strip() for. url in f.readlines()]


    def parse (self, response):
        items = BankdataItem()
                                                                          #for rows response.xpath('//*[@class="table table-striped"]//tbody/tr'):
          title = response.css('title::text()').extract()
          headings = reponse.xpath('//th[1]/text()').extract()
          sno = reponse.xpath('//td[3]/text()').extract()
          particulars =reponse.xpath('//td[3]/text()').extract()
          details = reponse.xpath('//td[3]/text()').extract()
          charges = reponse.xpath('//td[4]/text()').extract()




           items['title'] = title
           items['headings'] = headings
           items['sno'] = sno
           items['particulars'] = particulars
           items ['details'] = details
           items['charges'] = charges

               yield items                         #dictionary definition

            # next_page= response.xpath().extract()
            # if next_page is not None:
            # next_page_link = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page_link ,callback=self.parse)