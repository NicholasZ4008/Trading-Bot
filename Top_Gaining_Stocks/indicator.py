import yfinance as yf
import pandas as pd
import time

def indicator_for_setup():
    start_time = time.time()
    gaining_stocks_df = pd.read_csv('gaining_stocks.csv')

    symbol_array = []
    open_array = []
    high_array = []
    low_array = []
    volume_array = []
    date_array = []
    closing_array = []

    for symbol in gaining_stocks_df['stock_symbol']:
        stock = yf.Ticker(symbol)
        history_one_year = stock.history(period='1y')
        for index, row in history_one_year.iterrows():
            date_array.append(index)
            open_array.append(row['Open'])
            high_array.append(row['High'])
            low_array.append(row['Low'])
            volume_array.append(row['Volume'])
            symbol_array.append(symbol)
            closing_array.append(row['Close'])

    yearly_historic_df = pd.DataFrame({
        'Symbol': symbol_array,
        'Date': date_array,
        'Open': open_array,
        'Close': closing_array,
        'High': high_array,
        'Low': low_array,
        'Volume': volume_array
    })

    yearly_historic_df['Date'] = pd.to_datetime(yearly_historic_df['Date'], utc=True).dt.tz_convert(None)
    yearly_historic_df.sort_values(by=['Symbol', 'Date'], inplace=True)
    yearly_historic_df.loc[:, 'Price_Change'] = yearly_historic_df.groupby('Symbol')['Close'].transform(lambda x: x.pct_change())
    yearly_historic_df.loc[:, 'Support_Level'] = yearly_historic_df.groupby('Symbol')['Low'].transform(lambda x: x.rolling(window=50).min())
    yearly_historic_df.loc[:, 'Resistance_Level'] = yearly_historic_df.groupby('Symbol')['High'].transform(lambda x: x.rolling(window=50).max())
    yearly_historic_df['50_EMA'] = yearly_historic_df.groupby('Symbol')['Close'].transform(lambda x: x.ewm(span=50, adjust=False).mean())
    yearly_historic_df.dropna(subset=['50_EMA', 'Support_Level', 'Resistance_Level', 'Price_Change'], inplace=True)
    
    top_stocks_ema=yearly_historic_df.copy()
    # Generate buy, sell and hold signals
    top_stocks_ema.loc[:, 'Decisions'] = 'Hold'  # default to 'Hold'
    top_stocks_ema.loc[((top_stocks_ema['Close'] > top_stocks_ema['50_EMA']) & (top_stocks_ema['Close'].shift(1) < top_stocks_ema['50_EMA'].shift(1))) & ((top_stocks_ema['Close'].shift(1) <= top_stocks_ema['Support_Level'].shift(1)) & (top_stocks_ema['Price_Change'] > 0)), 'Decisions'] = 'Buy'
    top_stocks_ema.loc[((top_stocks_ema['Close'] < top_stocks_ema['50_EMA']) & (top_stocks_ema['Close'].shift(1) > top_stocks_ema['50_EMA'].shift(1))) & ((top_stocks_ema['Close'].shift(1) >= top_stocks_ema['Resistance_Level'].shift(1)) & (top_stocks_ema['Price_Change'] < 0)), 'Decisions'] = 'Sell'


    top_stocks_ema.to_csv('training_dataset.csv',index=False)


'''
Exponential Moving Average (EMA) crossovers. In this case, a 50-day EMA is used. The EMA is a type of moving average that gives more weight to recent prices, which can make it more responsive to new information compared to a Simple Moving Average (SMA).

The Sell_Signal being True indicates an EMA crossover where the closing price of the stock has moved from above the 50-day EMA (on the previous day) to below the 50-day EMA (on the current day). This is often interpreted as a bearish signal.

A bearish signal suggests that the price of the stock may decrease in the future. The term “bearish” comes from the behavior of a bear, swiping downward with its paws, symbolizing falling prices. Traders who believe that a stock’s price will decrease are said to be bearish on the stock.
In the context of this strategy, a Sell_Signal being True indicates that the stock’s closing price has crossed below its 50-day Exponential Moving Average (EMA). Some traders interpret this as a bearish signal, suggesting that the stock’s price may decrease in the future.

In response to such a signal, a trader might decide to sell the stock to potentially avoid further losses if the price continues to decline.

For a Buy_Signal, you look that the current closing price is greater than the current 50 day period exponential moving average and the previous closing price was less than than the previous 50 day exponential moving average
--50 day window size over a year's data

What the indicator script is doing: This script performs a technical analysis on historical stock data to identify potential buy and sell signals based on Exponential Moving Average (EMA) crossovers and support and resistance levels. The top 3 stocks are selected based on their rate of return, volume, and volatility. The script then calculates the 50-day EMA for each of the top stocks and generates buy and sell signals based on EMA crossovers. It also identifies the support and resistance levels for each of the top stocks and confirms the buy and sell signals based on these levels. 

'''