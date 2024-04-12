import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import numpy as np

def getting_gaining_stocks():
    df = pd.read_csv('dataset.csv')
    pages = []
    stock_name_array = []
    stock_url_array = []
    stock_symbol_array = []
    values_list = []
    new_value = []
    row_values = []
    offset = 0
    # offset<=175
    while(offset <= 25):
        url = f'https://ca.finance.yahoo.com/gainers/?count=25&offset={offset}'
        pages.append(url)
        offset += 25

    for page_url in pages:
        webpage = requests.get(page_url)
        soup = bs(webpage.text, 'html.parser')
        stock_table = soup.find('table', class_='W(100%)')
        if stock_table:
            tr_tags = stock_table.find_all('tr')

            for tr_tag in tr_tags:
                td_tag = tr_tag.find('td')
                if td_tag:
                    a_tag = td_tag.find('a', attrs={'data-test': 'quoteLink'})
                    if a_tag:
                        stock_symbol = a_tag.text
                        stock_url = a_tag['href']
                        stock_name = a_tag['title']
                        stock_name_array.append(stock_name)
                        stock_url_array.append(stock_url)
                        stock_symbol_array.append(stock_symbol)

    gaining_stocks_df = pd.DataFrame({'stock_symbol': stock_symbol_array, 'stock_url': stock_url_array, 'stock_name': stock_name_array})

    gaining_stocks_df.to_csv('gaining_stocks.csv')


