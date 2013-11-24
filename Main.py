import YellScraper

scraper = YellScraper.Scraper()
scraper.setKeyword('Restaurant')
scraper.setLocation('Old+Street%2C+ec1v')
scraper.start()
print 'Done... Exiting'