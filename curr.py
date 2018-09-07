import bs4, requests, json, csv

currList = ['USD_GBP', 'USD_JPY', 'USD_MXN', 'USD_EUR', 'USD_CNY',
            'USD_KHR', 'USD_HRK', 'USD_CZK', 'USD_CAD']

for x in currList:
    my_url = "http://free.currencyconverterapi.com/api/v5/convert?q=" + x + "&compact=y"
    r = requests.get(my_url)
    page_html = r.text
    page_html = json.loads(page_html)
    page_html = page_html[x]
    print(page_html['val'])

#github changes
