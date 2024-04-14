import yfinance as yf
import pandas as pd
import time

def indicator_for_setup():
    start_time=time.time()
    gaining_stocks_df=pd.read_csv('dataset_smp500.csv')
    symbol_array=[]
    Open_array=[]
    High_array=[]
    Low_array=[]
    Volume_array=[]
    Date_array=[]
    Symbol_array=[]
    Closing_array=[]

    for symbol in gaining_stocks_df['stock_symbol']:
        stock = yf.Ticker(symbol)
        history_one_year = stock.history(period='1y')
        for index, row in history_one_year.iterrows():
            Date_array.append(index)
            Open_array.append(row['Open'])
            High_array.append(row['High'])
            Low_array.append(row['Low'])
            Volume_array.append(row['Volume'])
            Symbol_array.append(symbol)
            Closing_array.append(row['Close'])

    yearly_historic_df=pd.DataFrame({'Symbol': Symbol_array,'Date': Date_array, 'Open': Open_array, 'Close':Closing_array, 'High':High_array, 'Low':Low_array,'Volume': Volume_array})

    yearly_historic_df['Date'] = pd.to_datetime(yearly_historic_df['Date'])

    # Sort the dataframe by 'Symbol' and 'Date'
    yearly_historic_df.sort_values(by=['Symbol', 'Date'], inplace=True)
    
    yearly_historic_df.to_csv('raw_yearly_yahoo_finance.csv')