from web_scraper_SMP500 import scrape, format_raw

def main():
    raw = scrape()
    smp500_df=format_raw(raw)
    smp500_df.to_csv('dataset_smp500.csv', index=False)
    
if __name__=='__main__':
    main()