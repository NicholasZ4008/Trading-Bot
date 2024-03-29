import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# confirmed sell signal is like me setting a stop loss, as there volatile stocks, so we wanna sell as soon as theres negative growth and when price stock falls to limit losses
#  confirmed buy
buy_indicator_data=pd.read_csv('Confirmed_Buy_Signal')
sell_indicator_data=pd.read_csv('Confirmed_Sell_Signal')

# if my 50 period EMA based buy/sell signal coincides with my support/resistance level based buy/sell signal, meaning for example ones buy signal is true and the others is false, or ones sell signal is true and the others is false, and vice versa, then put it on hold. If both are True or if both are False, follow through with buy or sell based on the signal

'''
Buy/Sell Signal Based on 50-day EMA: Use the "Buy_Signal" and "Sell_Signal" columns to determine whether a buy or sell signal is indicated based on the 50-day Exponential Moving Average (EMA).

Buy/Sell Signal Based on Support/Resistance Levels: Use the "Confirmed_Buy_Signal" and "Confirmed_Sell_Signal" columns to determine whether a buy or sell signal is confirmed based on support and resistance levels.

Label Assignment:

If the buy signal is True based on the 50-day EMA and False based on support/resistance levels (or vice versa), label the instance as "Hold."
If both buy signals are True or both are False, follow through with the buy or sell signal based on the signal.
If the sell signal is True based on the 50-day EMA and False based on support/resistance levels (or vice versa), label the instance as "Hold."
By following this labeling approach, you'll be incorporating both the 50-day EMA signals and the support/resistance level signals to determine whether to buy, sell, or hold the stock.
'''

buy_signal_values=buy_indicator_data['Buy_Signal'].values
confirmed_buy_signal_values=buy_indicator_data['Confirmed_Buy_Signal'].values
hold_array_buy=[]

for i in range(len(buy_signal_values)):
    if buy_signal_values[i]!=confirmed_buy_signal_values[i]:
     hold_array_buy.append(True)
    else:
        hold_array_buy.append(False)
buy_indicator_data['Hold_Signal']=hold_array_buy


sell_signal_values=sell_indicator_data['Sell_Signal'].values
confirmed_sell_signal_values=sell_indicator_data['Confirmed_Sell_Signal'].values

hold_array_sell=[]
for j in range(len(sell_signal_values)):
    if sell_signal_values[j]!=confirmed_sell_signal_values[j]:
        hold_array_sell.append(True)
    else:
        hold_array_sell.append(False)
sell_indicator_data['Hold_Signal']=hold_array_sell



decision_array_1=[]
for c in range(len(hold_array_buy)):
    if hold_array_buy[c]==True:
        decision_array_1.append('hold')
    else:
        decision_array_1.append('buy')
        
decision_array_2=[]
for k in range(len(hold_array_sell)):
    if hold_array_sell[k]==True:
        decision_array_2.append('hold')
    else:
        decision_array_2.append('sell')
        
buy_indicator_data['decision']=decision_array_1
sell_indicator_data['decision']=decision_array_2
    
buy_indicator_data.drop(columns=['Buy_Signal', 'Sell_Signal', 'Confirmed_Buy_Signal', 'Confirmed_Sell_Signal', 'Hold_Signal','Unnamed: 0'], inplace=True)
sell_indicator_data.drop(columns=['Buy_Signal', 'Sell_Signal', 'Confirmed_Buy_Signal', 'Confirmed_Sell_Signal', 'Hold_Signal','Unnamed: 0'], inplace=True)

merged_data = pd.concat([buy_indicator_data, sell_indicator_data], ignore_index=True)

X = merged_data.drop(columns=['decision', 'Date'])
y = merged_data['decision']

# Encode the 'Symbol' column
encoder = OneHotEncoder()
X_encoded = pd.concat([X.drop(columns=['Symbol']), pd.get_dummies(X['Symbol'])], axis=1)

X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


'''
Performing Logistic Regression:

Once the model is trained, you use it to predict the labels for the test set (X_test_scaled). These predicted labels (y_pred) are then compared with the actual labels in the test set (y_test). The accuracy of the model is calculated by comparing the predicted labels with the true labels in the test set using the accuracy_score function.

To clarify:

The model is trained using the training data (X_train_scaled and y_train).
The trained model is then used to predict labels for the test data (X_test_scaled).
Finally, the accuracy of the model is calculated by comparing the predicted labels with the actual labels in the test set (y_test).
The accuracy score represents the proportion of correctly classified samples in the test set. It provides an estimate of how well the model generalizes to unseen data.
'''



# do other classification models such as Random Forest Calssfier, Support Bector Machines (SVM), Gradient Boosting Classifier (XGBoost, LightGBM, or CatBoost)
# change up classification, instead of buy, sell and hold, could do rise, fall, stay the same