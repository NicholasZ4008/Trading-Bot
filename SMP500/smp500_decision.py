import pandas as pd

def decisions():
    # Load the data into a DataFrame
    df = pd.read_csv('test.csv')

    # Convert the date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Set the date column as the index
    df.set_index('Date', inplace=True)

    # Calculate the moving average
    window_size = 200  # Change this to 50 or 200 for your use case
    df['moving_average'] = df['Close'].rolling(window=window_size).mean()

    # Determine the trend
    df['trend'] = 'stagnant'
    df.loc[df['Close'] > df['moving_average'], 'trend'] = 'raising'
    df.loc[df['Close'] < df['moving_average'], 'trend'] = 'falling'

    # Print the results
    df.to_csv('decisions.csv')
