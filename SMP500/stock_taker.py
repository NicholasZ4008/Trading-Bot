import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from model import model_analysis
stock_symbol = input("Enter Stock Symbol: ")
print('Loading Details:', stock_symbol)
stock = yf.Ticker(stock_symbol)
history_one_year = stock.history(period='1y')
if history_one_year.empty:
    print("Stock Symbol doesn't exist or no data available. Try again later!")
else:
    date_array = history_one_year.index.tolist()
    open_array = history_one_year['Open'].tolist()
    high_array = history_one_year['High'].tolist()
    low_array = history_one_year['Low'].tolist()
    volume_array = history_one_year['Volume'].tolist()
    closing_array = history_one_year['Close'].tolist()
    symbol_array = [stock_symbol] * len(date_array)

    yearly_historic_df = pd.DataFrame({
        'Symbol': symbol_array,
        'Date': date_array,
        'Open': open_array,
        'Close': closing_array,
        'High': high_array,
        'Low': low_array,
        'Volume': volume_array
    })
    yearly_historic_df['Date'] = pd.to_datetime(yearly_historic_df['Date'])
    yearly_historic_df.sort_values(by=['Symbol', 'Date'], inplace=True)

    # Calculate the 50-day simple moving average
    yearly_historic_df['50_MA'] = yearly_historic_df.groupby('Symbol')['Close'].rolling(window=50).mean().reset_index(drop=True)
    yearly_historic_df.dropna(subset=['50_MA'], inplace=True)  # Ensure there's enough data
    data = yearly_historic_df.drop(columns=['Symbol', 'Date'])
    
    # Load trained DecisionTreeClassifier model
    dtc_model = model_analysis(use_only_dtc=True)
    prediction = dtc_model.predict(data.iloc[-1:])  # Predict using the latest data point
    print("Prediction for today's stock movement based on DecisionTreeClassifier:")
    predicted_label = prediction[0]
    print("Rising, Current day closing price was greater than the 50 day moving average of closing prices" if predicted_label == 'Rising' else "Falling, Current day closing price was less than the 50 day moving average of closing prices" if predicted_label == 'Falling' else "Stagnant, Closing Price is equal to the 50 day moving average of closing prices")

    plt.figure(figsize=(14, 7))
    plt.plot(yearly_historic_df['Date'], yearly_historic_df['Close'], label='Close Price')
    plt.plot(yearly_historic_df['Date'], yearly_historic_df['50_MA'], label='50-Day SMA', linestyle='--')
    plt.title(f"{stock_symbol} Stock Price and 50-Day SMA")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    
    # Save the figure as a PNG file
    plt.savefig(f"{stock_symbol}_Stock_Price_and_SMA.png")
    print(f"Plot saved as {stock_symbol}_Stock_Price_and_SMA.png")
