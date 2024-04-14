from web_scraper_SMP500 import scrape, format_raw
from indicator_smp500 import indicator_for_setup
from smp500_decision import decisions, moving_average_plot
from model import model_analysis

def main():
    raw = scrape() #Webscrape all of S&P500 stocks from Slick Charts
    smp500_df=format_raw(raw) #Format all webscraped stocks into dataframe with appropriate features
    smp500_df.to_csv('dataset_smp500.csv', index=False) #Save smp500_df to a usable csv across all files
    indicator_for_setup() #Take in dataset_smp500.csv and use technical indicators, and 1 year of historic stock data for each stock and set up training features and save to dataset "raw_yearly_yahoo_finance.csv"
    decisions() # Take in raw_yearly_yahoo_finance.csv and conduct moving average algorithm and further enhance training data and save to "decisions.csv"
    model_analysis() #Take in csv decisions.csv and train classification models with training features
    moving_average_plot() #Display 50 day rolling moving average window on Apple stock for further demonstration of technical indicators
    
if __name__=='__main__':
    main()