import requests, json, csv, time

#Currency List (random order)
currList = ['USD_GBP', 'USD_JPY', 'USD_MXN', 'USD_EUR', 'USD_CNY',
            'USD_KHR', 'USD_HRK', 'USD_CZK', 'USD_CAD', 'USD_AWG',
            'USD_RUB', 'USD_KES', 'USD_XAF', 'USD_TMT', 'USD_KYD',
            'USD_SGD', 'USD_CVE', 'USD_BND', 'USD_CLP', 'USD_NZD', 
            'USD_XOF', 'USD_DOP', 'USD_EGP', 'USD_CZK', 'USD_ANG', 
            'USD_CUC', 'USD_CUP', 'USD_XCD', 'USD_DKK', 'USD_XAF',
            'USD_GMD', 'USD_XPF', 'USD_GEL', 'USD_AED', 'USD_UGX']

#request to pull http from webportal, extracts currency from json, parses to format and saves to csv file
for fx in currList:
    #loading, extracting & parsing
    my_url = "http://free.currencyconverterapi.com/api/v5/convert?q=" + fx + "&compact=y"
    r = requests.get(my_url)
    page_html = r.text
    page_html = json.loads(page_html)
    page_html = page_html[fx]
    page_html = page_html['val']
    page_html = str(page_html)
    #this method is used so that the website won't trigger a timeout due to the number of requests in currList
    time.sleep(.15)
    
    #CSV stuff
    with open('Output.csv', 'a', newline='') as newFile:
        csv_writer = csv.writer(newFile)
        insert = [fx] + [page_html]
        csv_writer.writerow(insert)
        print(fx + ' ' + page_html)