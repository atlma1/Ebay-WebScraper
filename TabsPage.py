
# get the name of the item
def item_name(soup):
    return soup.find("h1", class_="product-title").text


# getting the image
def item_image(soup):
    return soup.find("img", class_="vi-image-gallery__image vi-image-gallery__image--absolute-center")["src"]


# getting the price
def item_price(soup):
    return soup.find("div", class_="display-price").text


# getting the condition
def item_condition(soup):
    return soup.findAll("li", class_="item-highlight")[1].find("span").text


def item_seller(soup):
    return soup.find("div", class_="seller-persona").findAll("span")[1].find("a").text


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


def item_return_policy(soup):
    string = soup.findAll("li", class_="item-highlight")[2].text
    if string.find("\xa0") != -1:
        return string.replace(u'\xa0', u' ')
    else:
        return string


def item_attributes(soup):
    product = {"item_name": item_name(soup), "item_image": item_image(soup),
               "item_price": item_price(soup), "item_condition": item_condition(soup),
               "item_seller": item_seller(soup), "item_availability": item_availability(soup),
               "item return_policy": item_return_policy(soup)}
    return product
