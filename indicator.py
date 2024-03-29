import yfinance as yf
import pandas as pd
import time
def indicator_for_setup():
    start_time=time.time()
    gaining_stocks_df=pd.read_csv('gaining_stocks.csv')
    symbol_array=[]
    Open_array=[]
    High_array=[]
    Low_array=[]
    Volume_array=[]
    Date_array=[]
    Symbol_array=[]
    Closing_array=[]
    historic_df=pd.DataFrame({'historic_data':[]})

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

    yearly_historic_df['Return'] = yearly_historic_df.groupby('Symbol')['Close'].transform(lambda x: x.pct_change().add(1).cumprod())
    # Calculate the standard deviation of the daily returns (volatility)
    yearly_historic_df['Return_pct'] = yearly_historic_df.groupby('Symbol')['Close'].pct_change()
    yearly_historic_df['Volatility'] = yearly_historic_df.groupby('Symbol')['Return_pct'].transform(lambda x: x.rolling(window=50).std())

    # Calculate the average volume
    yearly_historic_df['Avg_Volume'] = yearly_historic_df.groupby('Symbol')['Volume'].transform(lambda x: x.rolling(window=50).mean())
    # Get the final rate of return for each stock
    final_returns = yearly_historic_df.groupby('Symbol')['Return'].last()
    final_avg_volume = yearly_historic_df.groupby('Symbol')['Avg_Volume'].last()
    final_volatility = yearly_historic_df.groupby('Symbol')['Volatility'].last()
    stock_stats = pd.DataFrame({
        'Return': final_returns,
        'Avg_Volume': final_avg_volume,
        'Volatility': final_volatility
    })
    top_stocks = stock_stats.sort_values(by=['Return', 'Avg_Volume', 'Volatility'], ascending=[False, False, True]).head(3)

    top_symbols = top_stocks.index

    # Calculate the 50-day EMA (Exponential Moving Average) only for the top stocks
    top_stocks_ema = yearly_historic_df[yearly_historic_df['Symbol'].isin(top_symbols)].copy()
    top_stocks_ema['50_EMA'] = top_stocks_ema.groupby('Symbol')['Close'].transform(lambda x: x.ewm(span=50).mean())

    # Generate buy and sell signals. Based off EMA crossover
    top_stocks_ema['Buy_Signal'] = (top_stocks_ema['Close'] > top_stocks_ema['50_EMA']) & (top_stocks_ema['Close'].shift(1) < top_stocks_ema['50_EMA'].shift(1))
    top_stocks_ema['Sell_Signal'] = (top_stocks_ema['Close'] < top_stocks_ema['50_EMA']) & (top_stocks_ema['Close'].shift(1) > top_stocks_ema['50_EMA'].shift(1))

    # Identify support and resistance levels
    top_stocks_ema['Support_Level'] = top_stocks_ema.groupby('Symbol')['Low'].transform(lambda x: x.rolling(window=50).min())
    top_stocks_ema['Resistance_Level'] = top_stocks_ema.groupby('Symbol')['High'].transform(lambda x: x.rolling(window=50).max())

    buy_signals = top_stocks_ema[top_stocks_ema['Buy_Signal']]
    sell_signals = top_stocks_ema[top_stocks_ema['Sell_Signal']]

    # using ema and (resistance and support levels)


    top_stocks_ema['Price_Change'] = top_stocks_ema.groupby('Symbol')['Close'].transform(lambda x: x.pct_change())

    # Generate a sell signal when the price starts to decrease after reaching the resistance level. Also buy when price of stocks falls under or equals support level and starts to see an increase 
    top_stocks_ema['Confirmed_Buy_Signal'] = ((top_stocks_ema['Close'].shift(1) <= top_stocks_ema['Support_Level'].shift(1)) & (top_stocks_ema['Price_Change'] > 0))
    top_stocks_ema['Confirmed_Sell_Signal'] = ((top_stocks_ema['Close'].shift(1) >= top_stocks_ema['Resistance_Level'].shift(1)) & (top_stocks_ema['Price_Change'] < 0))
    Confirmed_Buy_Signal=top_stocks_ema[top_stocks_ema['Confirmed_Buy_Signal'] ]
    Confirmed_Sell_Signal=top_stocks_ema[top_stocks_ema['Confirmed_Sell_Signal']]

    print(time.time()-start_time,' seconds to finish\n')   
    
    Confirmed_Buy_Signal.to_csv('Confirmed_Buy_Signal')
    Confirmed_Sell_Signal.to_csv('Confirmed_Sell_Signal')
     
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