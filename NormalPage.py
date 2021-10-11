from bs4 import BeautifulSoup
import requests
import time
import concurrent.futures

# take in product page link, return beautifulsoup object
def turn_to_soup(input_url):
    time.sleep(1)
    html = requests.get(input_url)
    return BeautifulSoup(html.text, 'lxml')


# get the name of the item
def item_name(soup):
    try:
        return soup.find("h1", class_="it-ttl").contents[1]
    except AttributeError:
        return soup.find("h1", class_="product-title").text


# getting the image
def item_image(soup):
    try:
        return soup.find("img", class_="img img300")["src"]
    except TypeError:
        return soup.find("a", class_="vi-image-gallery__enlarge-link").find("img")["data-src"]


# getting the price
def item_price(soup):
    return soup.find("span", class_="notranslate")["content"]


# getting the condition
def item_condition(soup):
    return soup.find("div", class_="u-flL condText").text


# getting the seller
def item_seller(soup):
    try:
        return soup.find("span", class_="mbg-nw").text
    except AttributeError:
        return soup.findAll("span", class_="no-wrap")[1].find("a")["title"]


# getting the availability
def item_availability(soup):
    soup1 = soup.find("span", class_="qtyTxt vi-bboxrev-dsplblk vi-qty-fixAlignment feedbackON")
    if soup1 is None:
        soup2 = soup.find("span", class_="qtyTxt vi-bboxrev-dsplblk vi-qty-fixAlignment feedbackON vi-vpqp-feedback")
        if soup2 is None:
            return "N/A"
        else:
            return soup2.find("span", class_="").text.strip()
    else:
        return soup1.find("span", class_="").text.strip()


# getting the return policy
def item_return_policy(soup):
    try:
        string = soup.find("td", class_="rpWrapCol").find("span").find("span").text
        if string.find("\xa0") != -1:
            return string.replace(u'\xa0', u' ')
        else:
            return string

    except AttributeError:
        return soup.find("td", class_="rpWrapCol").find("span").text


# returns a dictionary with all of the attributes of the product
def item_attributes(soup):
    product = {"item_name": item_name(soup), "item_image": item_image(soup),
               "item_price": item_price(soup), "item_condition": item_condition(soup),
               "item_seller": item_seller(soup), "item_availability": item_availability(soup),
               "item_return_policy": item_return_policy(soup)}
    return product

