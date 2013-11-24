import urllib
import time
import sys
from bs4 import BeautifulSoup

class Scraper:
        pages = []
        keyword = ""
        location = ""
        results = []

        def setKeyword(self,keywordInput):
                self.keyword = keywordInput

        def setLocation(self,locationInput):
                self.location = locationInput

        def createPages(self):
                if self.keyword != "" and self.location != "":
                        for i in range(1,10):
                                page = 'http://www.yell.com/ucs/UcsSearchAction.do?keywords='+self.keyword+'&location='+self.location+'&pageNum=%s' % i
                                self.pages.append(page)
                else:
                        print "Location or Keyword not set\nUse setKeyword or setLocation functions before continuing"
                        sys.exit(0)

        def start(self):
                self.createPages()
                if self.pages:
                        for page in self.pages:
                                f = urllib.urlopen(page)
                                f = f.read()
                                soup = BeautifulSoup(f)
                                listings = soup.find_all("div", class_="parentListing")
                                if len(listings) > 0:
                                    for listing in listings:
                                        company = {}

                                        #name
                                        company['name'] = listing.find('a', itemprop="name").get_text(strip=True)

                                        #number
                                        company['number'] = listing.select('.l-telephone ul li strong')[0].string

                                        #address
                                        company['address'] = listing.find('span', itemprop="streetAddress").get_text(strip=True) + ' ' + listing.find('span', itemprop="addressLocality").get_text(strip=True) + ', ' + listing.find('span', itemprop="postalCode").get_text(strip=True)

                                        #add company
                                        self.results.append(company)

                                #keep yell.com happy
                                time.sleep(15)
                        return self.results