import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import numpy as np

'''
Pipeline:
01-scrape-data.py
02-clean-missing-fields.py
03-generate-features.py
04-train-model.py
05-score-model.py
06-generate-plots.py
'''
# making HTTP requests to the right URLs and getting back responses (WEB APIS)
def getting_data():
    start_time=time.time()
    pages=[]
    # url endings have different page numbers, gather up to page 1 to 4 urls and append to pages
    for page_number in range(1,10):
        url_start='https://www.centralcharts.com/en/price-list-ranking/'
        url_end='ALL/desc/ts_19-us-nasdaq-stocks--qc_3-previous-close-change?p='
        url=url_start+url_end + str(page_number)
        pages.append(url)
    
    rate_limit=1
    values_list=[]
    # for each url in pages array, send a request to the server url and extract data into workable format
    # bs html parser, then inspect element of webpage, found the table with all the stocks inside, class name of table is 'tabMini tabQuotes'
    # parse through table, seperate by stocks, as each stock has its own category/indice, seperated by tr tags
    # inside tr tags, there's td tags, representing table information. Want to extract these to pull out the stock information
    # tr tag represents a row in the table (table row), and then the td is the individual data pieces part of the row, so the data information pertaining to the stock (row)
    for page in pages:
        webpage= requests.get(page)
        soup=bs(webpage.text, 'html.parser')
        
        stock_table=soup.find('table',class_='tabMini tabQuotes')
        tr_tag_list=stock_table.find_all('tr')
        for each_tr_tag in tr_tag_list[1:]:
            td_tag_list=each_tr_tag.find_all('td')
            row_values=[]
            for each_td_tag in td_tag_list[0:7]:
                new_value=each_td_tag.text.strip()
                row_values.append(new_value)
            values_list.append(row_values)
        time.sleep(1/rate_limit)
    # print(values_list)
    print('--- %s seconds ---' %(time.time()-start_time))
    return values_list

def DataFrame_formatting(values_list):
    stock_name = []
    current_price = []
    change_percent = []
    opening_price = []
    highest_price_inday = []
    lowest_price_inday = []
    volume_inday = []
    
    for stock in values_list:
        for i in range(len(stock)):
            if i == 0:
                stock_name.append(stock[i])
            elif i == 1:
                current_price.append(stock[i])
            elif i == 2:
                change_percent.append(stock[i])
            elif i == 3:
                opening_price.append(stock[i])
            elif i == 4:
                highest_price_inday.append(stock[i])
            elif i == 5:
                lowest_price_inday.append(stock[i])
            elif i == 6:
                volume_inday.append(stock[i])
                
    stock_df = pd.DataFrame({
        'stock_name': stock_name,
        'current_price': current_price,
        'change_percent': change_percent,
        'opening_price': opening_price,
        'closing_highest_price': highest_price_inday,
        'closing_lowest_price': lowest_price_inday,
        'closing_volume_traded': volume_inday
    })
    return stock_df

    print(stock_df)
    print(stock_df.head())
    print(stock_df.info())
    