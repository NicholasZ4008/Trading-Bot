# Trading-Bot

1.Data Collection and Cleaning: • Getting historical market data from various sources like Yahoo Finance, Alpha Vantage, or other financial APIs. Web scraping is also an option to form live market databases • Cleaning the data to remove any inconsistencies, missing values, or outliers. This involves utilizing skills learned in the "Data In Python", "Getting Data", "Cleaning Data", and "Noise Filtering" modules.

2.Data Analysis Pipeline: • Developing a pipeline to analyze the historical market data, which includes extracting relevant features, performing statistical analysis, and generating insights. This involves applying the concepts learned in the "Data Analysis Pipeline", "Stats Review", "Inferential Stats", and "Statistical Tests" modules.

3.Machine Learning for Prediction: • Implementing machine learning models for predicting future market movements or identifying trading opportunities. This includes utilizing techniques covered in the "Machine Learning" and "ML: Classification" modules.

4.Big Data Processing (Optional): • For handling a huge database of historical market data, leveraging technologies like Spark for big data processing. This includes understanding concepts taught in the "Big Data and Spark" and "Working With Spark" modules.

5.Risk Management and Strategy Implementation: • Implementing risk management strategies to minimize potential losses and optimize trading performance. This could involve applying various risk management techniques discussed in class. • Implementing trading strategies based on the insights gained from data analysis and machine learning models. This involves understanding different trading strategies discussed in class and implementing them effectively.

6.Evaluation and Communication: • Evaluating the performance of the trading bot using backtesting and other evaluation metrics. • Communicating the results and findings effectively, which includes visualization of data and results. This involves skills learned in the "Communicating" module.

S&P500:

Running Instructions: All programs are already laid out ready to run in the main. 
Everything will run in sequence with this basic command.

python3 SMP500/main_smp500.py

Required libraries:
    selenium
    webdriver_manager
    bs4
    pandas
    time
    yfinance
    matplotlib
    scikit-learn

The expected files it will produce will be in this order:
1. dataset_smp500.csv
2. raw_yearly_yahoow_finance.csv
3. decisions.csv