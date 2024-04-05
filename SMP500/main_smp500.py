from web_scraper_SMP500 import scrape, format_raw
#from yahoofinance import getting_gaining_stocks
from indicator_smp500 import indicator_for_setup
from smp500_decision import decisions
from model import model_analysis

def main():
    raw = scrape()
    smp500_df=format_raw(raw)
    smp500_df.to_csv('dataset_smp500.csv', index=False)
    indicator_for_setup()
    decisions()
    model_analysis()
    
    
    
if __name__=='__main__':
    main()