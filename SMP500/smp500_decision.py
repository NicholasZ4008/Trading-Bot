import pandas as pd

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

