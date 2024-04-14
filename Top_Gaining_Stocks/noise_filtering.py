import pandas as pd
from statsmodels.nonparametric.smoothers_lowess import lowess
import matplotlib.pyplot as plt
from pykalman import KalmanFilter
import numpy as np

# perform LOESS Smoothing for price changes via (highest price reached before closing)-(starting day price). See what the common trend is.
# However, we want the financial instruments/stocks that lie above this linear line, beating the average, a strong positive outlier. 
# We also want to produce Loess smoothing for volume traded and see if we can find stocks with high volume of trading, and see if we can match them on the results of the previous LOESS
# see if we can match high volume traded stocks with high profit stocks, this will show if theres a correlation with price value and the volume being traded
# for volume traded, only get the stocks that have had a positive percent change, that means stocks probably going up, so a good volume ratio

def LOESS_smoothing(dataset):
    df = pd.read_csv(dataset)   
    stock_df = df.copy()
    stock_df['opening_price'] = pd.to_numeric(stock_df['opening_price'], errors='coerce')
    stock_df['closing_highest_price'] = pd.to_numeric(stock_df['closing_highest_price'], errors='coerce')
    stock_df['closing_lowest_price'] = pd.to_numeric(stock_df['closing_lowest_price'], errors='coerce')
    stock_df['closing_volume_traded'] = pd.to_numeric(stock_df['closing_volume_traded'].str.replace(',', ''), errors='coerce')    
    stock_df['change_percent'] = pd.to_numeric(stock_df['change_percent'], errors='coerce')    
    # Calculate profit margin
    stock_df['profit_margin'] = stock_df['closing_highest_price'] - stock_df['opening_price']

    # Plot data
    filtered_profit_margin = lowess(stock_df['profit_margin'], stock_df['closing_volume_traded'], frac=0.6)
    plt.plot(filtered_profit_margin[:, 0], filtered_profit_margin[:, 1], 'r-', linewidth=3)
    plt.xlabel('Volume Traded')
    plt.ylabel('Profit (Highest-opening)')
   
    # can help us understand if the volume being traded influenced our price margins



def Kalman_filtering(dataset):
    df = pd.read_csv(dataset)
    stock_df=df.copy()
    stock_df['closing_volume_traded'] = pd.to_numeric(stock_df['closing_volume_traded'].str.replace(',', ''), errors='coerce')
    closing_volume_traded = np.array(stock_df['closing_volume_traded'])

    # Initialize the Kalman Filter
    kf = KalmanFilter(
        initial_state_mean=closing_volume_traded[0],  # initial volume traded
        initial_state_covariance=0.1,  # small uncertainty in initial state
        observation_covariance=0.1,  # small measurement noise
        transition_covariance=1.0,  # larger process noise due to variability in volume traded
        transition_matrices=np.eye(1),  # assuming state transitions follow identity matrix
        n_dim_obs=1
    )

    # Use the observed values of the price to get a rolling mean
    state_means, _ = kf.filter(closing_volume_traded)

    # Plot original observation and estimated mean
    plt.plot(state_means)
    plt.plot(closing_volume_traded)
    plt.title('Kalman filter estimate of average')
    plt.legend(['Kalman Estimate', 'closing_volume_traded'])
    plt.xlabel('Stock Index')
    plt.ylabel('closing_volume_traded')
   

'''
If you’re confident in your initial volume traded, you can set the initial_state_covariance to a small value. This parameter represents your uncertainty in the initial state. A smaller value means you’re more confident in your initial state. For example, you could set it to 0.1 or even smaller depending on your level of confidence.

Measurement noise refers to the uncertainty or error in your measurements. In your case, this would be the closing_volume_traded values. Even if you’re confident in your data, there’s always some degree of uncertainty or noise in any real-world measurement. This could be due to various factors like fluctuations in the market, measurement errors, etc. The observation_covariance parameter in the Kalman filter represents this measurement noise. If you believe your measurements are very accurate, you can set this to a small value.

Process noise, on the other hand, refers to the uncertainty in the transitions of your system’s state. In your case, this would be the changes in closing_volume_traded from one time step to the next. The transition_covariance parameter in the Kalman filter represents this process noise. If the volume traded is hugely varying between each stock, you might want to set this to a larger value to account for this variability.
'''

'''
The “underlying state” of the volume traded is the true value of the volume traded that we would measure if there were no noise in our measurements. In reality, we can’t directly observe this underlying state because our measurements are always subject to some degree of noise or error. This noise could come from various sources, such as fluctuations in the market, measurement errors, etc.

The Kalman filter helps us estimate this underlying state from our noisy measurements. It does this by combining our current measurement and our previous estimate of the state in a statistically optimal way. This means it gives more weight to the measurement or estimate with less uncertainty.

So, when you apply the Kalman filter to your closing_volume_traded data, it’s trying to estimate the true closing_volume_traded values by reducing the noise in your measurements. The result is a smoothed time series that should give you a clearer picture of the underlying trend in the volume traded.

This can be useful in several ways:

Trend Identification: The smoothed time series can make it easier to identify underlying trends in the volume traded that might be obscured by noise in the raw data.
Anomaly Detection: If the smoothed time series significantly deviates from the raw data, it could indicate an anomaly or unusual trading activity.
Signal Extraction: The smoothed time series can be used as a signal in further analysis or in a trading algorithm. For example, sudden increases in the smoothed volume traded could be used as a signal to buy a stock.
Remember, the Kalman filter is just a tool and it’s up to you how to interpret and use its output. It’s always a good idea to understand the assumptions and limitations of any tool you’re using.
'''