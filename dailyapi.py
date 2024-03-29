import pandas as pd
import requests
df=pd.read_csv('dataset.csv')
apiKey='0M42BUFEDV9RRFBR'

for index, value in df['stock_name'].items():
    stock_name=value
    url_symbol=f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock_name}&apikey={apiKey}'
    symbol_response=requests.get(url_symbol)
    if symbol_response.status_code==200:
        stock_symbol=symbol_response.json()
        # stock_symbol=stock_symbol[0][0]
        print(stock_symbol)
    else:
        print('Stock not found')
    
    
    # url=f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={apiKey}'
    # response=requests.get(url)
    # if response.status_code==200:
    #     data=response.json()
    #     print(data)
    # else:
    #     print(f"Failed to fetch data for {stock_name}: {response.status_code}")
    
    

    
    
    