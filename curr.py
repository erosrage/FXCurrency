import requests, json, csv

currList = ['USD_GBP', 'USD_JPY', 'USD_MXN', 
            'USD_EUR', 'USD_CNY', 'USD_KHR', 
            'USD_HRK', 'USD_CZK', 'USD_CAD', 
            'USD_AWG', 'USD_RUB', 'USD_KES']

for fx in currList:
    my_url = "http://free.currencyconverterapi.com/api/v5/convert?q=" + fx + "&compact=y"
    
    r = requests.get(my_url)
    page_html = r.text

    page_html = json.loads(page_html)
    page_html = page_html[fx]
    page_html = page_html['val']

    with open('Output.csv', 'a', newline='') as newFile:
        csv_writer = csv.writer(newFile)
        insert = [fx] + [str(page_html)]
        csv_writer.writerow(insert)
        print(fx + ' ' + str(page_html))