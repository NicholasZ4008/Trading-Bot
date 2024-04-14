Project Description:
Our project automates the extraction and analysis of financial data to inform trading decisions. It begins by web scraping the top gaining and S&P 500 stocks from Yahoo Finance, capturing essential market dynamics. The data is then enhanced through the calculation of key technical indicators such as exponential moving averages, support and resistance levels, and incorporating fundamental attributes like open, close, high, low prices, volume, and price changes. These features serve as the foundation for training specialized classification models. For the highly volatile top gaining stocks, our models predict "Buy", "Sell", or "Hold" actions. For the more stable S&P 500 stocks, the models classify the stocks' movements as "Raising", "Falling", or "Stagnant". This dual approach allows for tailored strategies that address the distinct characteristics of each stock category, providing targeted insights for investors and traders alike.

Required Libraries:
Top_Gaining_Stocks:
beautifulsoup4==4.12.3
matplotlib==3.8.2
numpy==1.26.4
pandas==2.2.2
pykalman_py311_update==0.9.6
Requests==2.31.0
scikit_learn==1.4.1.post1
statsmodels==0.14.1
yfinance==0.2.37

from bs4 import BeautifulSoup  # for parsing HTML and XML documents
import matplotlib.pyplot as plt  # typical import for plotting with matplotlib
import numpy as np  # standard import for NumPy
import pandas as pd  # standard import for pandas
from pykalman import KalmanFilter  # importing KalmanFilter if using pykalman
import requests  # for making HTTP requests
from sklearn import datasets, linear_model  # example imports from scikit-learn
from statsmodels.nonparametric.smoothers_lowess import lowess
import yfinance as yf  # standard import for yfinance to fetch financial data
S&P500:
beautifulsoup4==4.12.3
matplotlib==3.8.2
pandas==2.2.2
Requests==2.31.0
scikit_learn==1.4.1.post1
selenium==4.19.0
webdriver_manager==4.0.1
yfinance==0.2.37

import bs4  # for BeautifulSoup
import matplotlib.pyplot as plt  # typical import for matplotlib
import pandas as pd  # standard pandas import
import requests  # for making HTTP requests
from sklearn import datasets, linear_model  # example import for scikit-learn
from selenium import webdriver  # import selenium webdriver
from webdriver_manager.chrome import ChromeDriverManager  # managing Chrome driver with webdriver_manager. Used for selenium
import yfinance as yf  # standard import for yfinance
