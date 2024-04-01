import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np

def scrape():
    page = []
    my_url = 'https://www.slickcharts.com/sp500'
    page.append(my_url)
    
    values_list = []
    
    webpage = requests.get(page)
    soup = bs(webpage.text , 'html.parser')
    
    stock_table = soup.find('table', class_= 'table table-hover table-borderless table-sm')
    tr_tag_list = stock_table.find_all('tr')
    
    for each_tr_tag in tr_tag_list[1:]:
        td_tag_list = each_tr_tag.find_all('td')
        
        row_values = []
        for each_td_tag in td_tag_list[0:7]:
            new_value = each_td_tag.text.strip()
            row_values.append(new_value)
        values_list.append(row_values)
     
    return(values_list)

def format_raw(raw):
    company_name = []
    stock_symbol = []
    portfolio_percent = []
    price = []
    flat_change = []
    percent_change = []
    
    for stock in raw:
        for i in range(len(stock)):
            if i == 0:
                company_name.append(stock[i])
            elif i == 1:
                stock_symbol.append(stock[i])
            elif i == 2:
                portfolio_percent.append(stock[i])
            elif i == 3:
                price.append(stock[i])
            elif i == 4:
                flat_change.append(stock[i])
            elif i == 5:
                percent_change.append(stock[i])
    
    smp500_df = pd.DataFrame({
        'company_name': company_name,
        'stock_symbol': stock_symbol,
        'portfolio_percent': portfolio_percent,
        'price': price,
        'flat_change': flat_change,
        'percent_change': percent_change,
    })
    
    return smp500_df
    