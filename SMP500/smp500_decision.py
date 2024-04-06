import pandas as pd
import matplotlib.dates as mdates
import matplotlib as plt

def decisions():
    # Load your dataframe containing historic stock data
    gaining_stocks_df = pd.read_csv('raw_yearly_yahoo_finance.csv')
    
    # Assuming 'price' column represents the closing price of the stock
    # Calculate the 200-day moving average for each stock
    moving_avg_df = gaining_stocks_df.groupby('Symbol')['Close'].rolling(window=200).mean().reset_index(level=0, drop=True)
    moving_avg_df = moving_avg_df.reset_index()  # Resetting the index
    
    # Rename the columns for clarity
    moving_avg_df.rename(columns={'Close': '200_MA'}, inplace=True)
    
    # Merge the moving average back into the original dataframe
    gaining_stocks_df = pd.merge(gaining_stocks_df, moving_avg_df, left_index=True, right_index=True, suffixes=('', '_MA'))
    
    def determine_decision(row):
        if row['Close'] > row['200_MA']:
            return 'Raising'
        elif row['Close'] < row['200_MA']:
            return 'Falling'
        else:
            return 'Stagnant'

    # Apply the function to each row to create the 'decision' column
    gaining_stocks_df['decision'] = gaining_stocks_df.apply(determine_decision, axis=1)

    # Save the updated dataframe
    gaining_stocks_df.to_csv('decisions.csv', index=False)

def moving_average_plot():
    
    decisions = pd.read_csv("decisions.csv")

    # Assuming 'Date' column is in the format 'YYYY-MM-DD'
    decisions.csv['Date'] = pd.to_datetime(decisions['Date'])

    # Plotting for a specific stock symbol, e.g., 'AAPL'
    aapl_df = decisions[decisions['Symbol'] == 'AAPL']

    plt.figure(figsize=(10, 6))
    plt.plot(aapl_df['Date'], aapl_df['Close'], label='Closing Price')
    plt.plot(aapl_df['Date'], aapl_df['200_MA'], label='200-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price and 200-Day Moving Average for AAPL')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gcf().autofmt_xdate()  # Rotation
    plt.show()


