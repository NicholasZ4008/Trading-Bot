import pandas as pd

def decisions():
    # Load your dataframe containing historic stock data
    gaining_stocks_df = pd.read_csv('test.csv')
    # Assuming 'price' column represents the closing price of the stock
    # Calculate the 200-day moving average for each stock
    gaining_stocks_df['200_MA'] = gaining_stocks_df.groupby('Symbol')['Close'].transform(lambda x: x.rolling(window=200).mean())
    def determine_decision(row):
        if row['close'] > row['200_MA']:
            return 'Raising'
        elif row['close'] < row['200_MA']:
            return 'Falling'
        else:
            return 'Stagnant'

    # Apply the function to each row to create the 'decision' column
    gaining_stocks_df['decision'] = gaining_stocks_df.apply(determine_decision, axis=1)

    # Save the updated dataframe
    gaining_stocks_df.to_csv('decisions.csv', index=False)

