from web_scraper import getting_data, DataFrame_formatting
from noise_filtering import LOESS_smoothing, Kalman_filtering
from yahoofinance import getting_gaining_stocks
from indicator import indicator_for_setup
from predictions import predictor
import matplotlib.pyplot as plt
def main():
    values_list = getting_data()
    stock_df=DataFrame_formatting(values_list)
    stock_df.to_csv('dataset.csv', index=False)  
    LOESS_smoothing('dataset.csv')
    plt.savefig('filtered_profit_margin_plot.png')
    plt.clf()
    Kalman_filtering('dataset.csv')
    plt.savefig('Volume_traded_true_state.png')
    plt.clf()
    getting_gaining_stocks()
    indicator_for_setup()
    predictor()
if __name__=='__main__':
    main()