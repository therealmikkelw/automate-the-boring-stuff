import bs4, requests


def getAmazonPrice(productUrl):

    # Using requests module to download a site on Amazon.com
    res = requests.get(productUrl)
    res.raise_for_status()

    # Parsing the downloaded site to a soup object
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Using CSS selector to access specific HTML tag
    # Find CSS selector F12 => right-click element => copy CSS selector
    elems = soup.select('span.a-color-price:nth-child(2)')

    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/')
print('The price is ' + price)
