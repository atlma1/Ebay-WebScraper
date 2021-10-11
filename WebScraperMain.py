import WebPageWebScraper
from WebPageWebScraper import PageParser
import NormalPage
import TabsPage


website = PageParser('https://www.ebay.com/b/Collectible-Funko-Bobbleheads-1970-Now/149372/bn_3017826')
print(website.parse_all())



