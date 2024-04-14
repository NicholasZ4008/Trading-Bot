import pandas as pd
import matplotlib.dates as mdates
import matplotlib.pyplot as plt


def determine_decision(row):
    if row['Close'] > row['50_MA']:
        return 'Raising'
    elif row['Close'] < row['50_MA']:
        return 'Falling'
    else:
        return 'Stagnant'


def decisions():
    gaining_stocks_df = pd.read_csv('raw_yearly_yahoo_finance.csv')
    
    gaining_stocks_df['Date'] = pd.to_datetime(gaining_stocks_df['Date'], utc=True).dt.tz_convert(None)

    gaining_stocks_df.sort_values(by=['Symbol', 'Date'], inplace=True)

    gaining_stocks_df['50_MA'] = gaining_stocks_df.groupby('Symbol')['Close'].rolling(window=50).mean().reset_index(drop=True)
    gaining_stocks_df.dropna(subset='50_MA', inplace=True)

    gaining_stocks_df['decision'] = gaining_stocks_df.apply(determine_decision, axis=1)

    gaining_stocks_df.to_csv('decisions.csv', index=False)


def moving_average_plot():
    decisions = pd.read_csv("decisions.csv")

    decisions['Date'] = pd.to_datetime(decisions['Date'])

    aapl_df = decisions[decisions['Symbol'] == 'AAPL']

    plt.figure(figsize=(10, 6))
    plt.plot(aapl_df['Date'], aapl_df['Close'], label='Closing Price')
    plt.plot(aapl_df['Date'], aapl_df['50_MA'], label='50-Day Moving Average')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price and 50-Day Moving Average for AAPL')
    plt.legend()
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.gcf().autofmt_xdate()

    plt.savefig('aapl_stock_and_ma.png')

    plt.show()


# decisions()
# moving_average_plot()