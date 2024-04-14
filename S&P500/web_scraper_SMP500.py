from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')  # Optional, for some headless environments
chrome_options.add_argument('--remote-debugging-port=9222')  # Optional, for debugging

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


def scrape():
    values_list = []

    global driver
    driver.get("https://www.slickcharts.com/sp500")
    time.sleep(5) 
    
    soup = bs(driver.page_source, 'html.parser')
    stock_table = soup.find('table', class_='table table-hover table-borderless table-sm')
    
    tr_tag_list = stock_table.find_all('tr')
    
    for each_tr_tag in tr_tag_list[1:]:
        td_tag_list = each_tr_tag.find_all('td')
        
        row_values = []
        for each_td_tag in td_tag_list[0:7]:
            new_value = each_td_tag.text.strip()
            row_values.append(new_value)
        values_list.append(row_values)
    
    return values_list


def format_raw(raw):
    index = []
    company_name = []
    stock_symbol = []
    portfolio_percent = []
    price = []
    flat_change = []
    percent_change = []
    
    for stock in raw:
        for i in range(len(stock)):
            if i == 0:
                index.append(stock[i])
            elif i == 1:
                company_name.append(stock[i])
            elif i == 2:
                stock_symbol.append(stock[i])
            elif i == 3:
                portfolio_percent.append(stock[i])
            elif i == 4:
                price.append(stock[i])
            elif i == 5:
                flat_change.append(stock[i])
            elif i == 6:
                percent_change.append(stock[i])
    
    smp500_df = pd.DataFrame({
        'index' : index,
        'company_name': company_name,
        'stock_symbol': stock_symbol,
        'portfolio_percent': portfolio_percent,
        'price': price,
        'flat_change': flat_change,
        'percent_change': percent_change,
    })
    
    return smp500_df
    