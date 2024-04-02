from web_scraper_SMP500 import scrape, format_raw
from yahoofinance_SMP500 import getting_gaining_stocks_smp500
from indicator import indicator_for_setup

def main():
    raw = scrape()
    smp500_df=format_raw(raw)
    smp500_df.to_csv('dataset_smp500.csv', index=False)
    getting_gaining_stocks_smp500()
    indicator_for_setup()
    
    
    
if __name__=='__main__':
    main()