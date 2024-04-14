# Project Description:
Our project automates the extraction and analysis of financial data to inform trading decisions. It begins by web scraping the top gaining and S&P 500 stocks from Yahoo Finance, capturing essential market dynamics. The data is then enhanced through the calculation of key technical indicators such as exponential moving averages, support and resistance levels, and incorporating fundamental attributes like open, close, high, low prices, volume, and price changes. These features serve as the foundation for training specialized classification models. For the highly volatile top gaining stocks, our models predict "Buy", "Sell", or "Hold" actions. For the more stable S&P 500 stocks, the models classify the stocks' movements as "Raising", "Falling", or "Stagnant". This dual approach allows for tailored strategies that address the distinct characteristics of each stock category, providing targeted insights for investors and traders alike.

# Required Libraries:
### **Top_Gaining_Stocks:**
  &emsp; **Dependencies** \
  &emsp; beautifulsoup4==4.12.3 \
  &emsp; matplotlib==3.8.2 \
  &emsp; numpy==1.26.4 \
  &emsp; pandas==2.2.2 \
  &emsp; pykalman_py311_update==0.9.6 \
  &emsp; Requests==2.31.0 \
  &emsp;  scikit_learn==1.4.1.post1 \
  &emsp; statsmodels==0.14.1 \
  &emsp; yfinance==0.2.37 

**Import Statements** \
 &emsp; from bs4 import BeautifulSoup  # for parsing HTML and XML documents \
 &emsp; import matplotlib.pyplot as plt  # typical import for plotting with matplotlib \
 &emsp; import numpy as np  # standard import for NumPy \
 &emsp; import pandas as pd  # standard import for pandas \
 &emsp; from pykalman import KalmanFilter  # importing KalmanFilter if using pykalman \
 &emsp; import requests  # for making HTTP requests \
 &emsp; from sklearn import datasets, linear_model  # example imports from scikit-learn \
 &emsp; from statsmodels.nonparametric.smoothers_lowess import lowess \
 &emsp; import yfinance as yf  # standard import for yfinance to fetch financial data 

### **S&P500:**
 &emsp; **Dependencies** \
 &emsp; beautifulsoup4==4.12.3 \
 &emsp; matplotlib==3.8.2 \
 &emsp; pandas==2.2.2 \
 &emsp; Requests==2.31.0 \
 &emsp; scikit_learn==1.4.1.post1 \
 &emsp; selenium==4.19.0 \
 &emsp; webdriver_manager==4.0.1 \
 &emsp; yfinance==0.2.37 

**Import Statements** \
 &emsp; import bs4  # for BeautifulSoup  \
 &emsp; import matplotlib.pyplot as plt  # typical import for matplotlib \
 &emsp; import pandas as pd  # standard pandas import \
 &emsp; import requests  # for making HTTP requests \
 &emsp; from sklearn import datasets, linear_model  # example import for scikit-learn \
 &emsp; from selenium import webdriver  # import selenium webdriver \
 &emsp; from webdriver_manager.chrome import ChromeDriverManager  # managing Chrome driver with webdriver_manager. Used for selenium \
 &emsp; import yfinance as yf  # standard import for yfinance 


# Order of Execution and How to Run:
## Top_Gaining_Stocks:
### main.py file:
	 ![image](https://github.com/AdamBahramiSchool/Trading-Bot/assets/145634016/9968a4e1-7aae-454d-86d6-5f47ecaa39f9)

Once in the Trading-Bot root directory, cd into the Top_Gaining_Stocks directory and in the terminal, run command ‘python3 main.py’
## S&P500:
 ### main_smp500.py file:
 	![alt text](https://github.com/[AdamBahramiSchool]/[Trading-Bot]/blob/[SMP500]/readme_images/smpmainpic.png?raw=true)

Once in the Trading-Bot root directory, cd into the S&P500 directory and in the terminal, run command ‘python3 main_smp500.py’


## Files produced/expected:
### Top_Gaining_Stocks:
1. dataset.csv 
2. filtered_profit_margin_plot.png 
3. Volume_traded_true_state.png 
4. gaining_stocks.csv 
5. training_dataset.csv 
Model scores will appear in terminal command line 

### SMP500:
1. dataset_smp500.csv 
2. raw_yearly_yahoow_finance.csv 
3. decisions.csv 
4. appl_stock_and_ma.png 
Model scores will appear in terminal command line 

## Video of Full execution: 


### ***Note***: 
1. In the current code we commented out the webscraping functions and left the latest preprocessed webscraped datasets right before the deadline, as SFU's network brings compilations when trying to do the HTTP requests due to IP limitations. Furthermore, there's a lot of compatability issues that arise with Selenium, therefore for a clean execution, we commented out the webscraping. However, in our video of execution, we show us webscraping the datasets, and further using them for our data analysis.

2. Furthermore, for our S&P500 models, we also commented out the MLPClassifier model as it takes more 5-10 minutes to execute. However, we show the results in our video of execution.

Warning: These can be uncommented and tested, but might pose problems. 
