from web_scraper import getting_data, DataFrame_formatting
from noise_filtering import LOESS_smoothing, Kalman_filtering
from yahoofinance import getting_gaining_stocks
from indicator import indicator_for_setup
from predictions import predictor
import matplotlib.pyplot as plt

# Uncomment values_list, stock_df, stock_df.tocsv and getting_gaining_stocks() to webscrape
def main():
    # values_list = getting_data() #Webscraping US Nasdaq stocks from Central Charts
    # stock_df=DataFrame_formatting(values_list) #Formatting the US Nasdaq webscraped stocks into dataframe with appropriate features
    # stock_df.to_csv('dataset.csv', index=False) #Saving formatted US Nasdaq stocks into usable dataset for all files
    LOESS_smoothing('dataset.csv') #Performing Loess Smoothing to understand if volume being traded influenced our price margins
    plt.savefig('filtered_profit_margin_plot.png') #Save Loess Smoothed chart
    plt.clf()
    Kalman_filtering('dataset.csv') #Performing Kalman Filter to understand the true underlying state of the volume being traded
    plt.savefig('Volume_traded_true_state.png')
    plt.clf()
    # getting_gaining_stocks() #Webscrape top 25 highest gaining stocks for the day from the yahoo finance website and save dataframe to csv "gaining_stocks.csv"
    indicator_for_setup() #Access "gaining_stocks.csv" and use indicators and 1 year of historic data of each of the top 25 Yahoo stocks to set up training features before training classification models and form a csv called training_dataset.csv
    predictor() #Takes in training_dataset.csv containing training features and trains classification models
if __name__=='__main__':
    main()