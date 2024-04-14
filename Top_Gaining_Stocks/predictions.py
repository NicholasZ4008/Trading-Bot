import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

def predictor():
    training_data = pd.read_csv('training_dataset.csv')
    target_variable = training_data['Decisions']
    training_data_filtered = training_data.drop(columns=['Date', 'Symbol', 'Decisions'])
    X_train, X_test, y_train, y_test = train_test_split(training_data_filtered, target_variable, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test) 
    Logistic_Regression(X_train_scaled, y_train, X_test_scaled, y_test)
    Random_Forest_Classifier(X_train_scaled, y_train, X_test_scaled, y_test)
    Support_Vector_Machine(X_train_scaled, y_train, X_test_scaled, y_test)

def Logistic_Regression(X_train_scaled,y_train,X_test_scaled, y_test):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    train_accuracy = model.score(X_train_scaled, y_train)
    test_accuracy = model.score(X_test_scaled, y_test)
    print("Training Accuracy of Logistic Regression:", train_accuracy)
    print("Test Accuracy of Logistic Regression:", test_accuracy,'\n')
    
    
def Random_Forest_Classifier(X_train_scaled,y_train,X_test_scaled, y_test):
    model=RandomForestClassifier()
    model.fit(X_train_scaled, y_train)
    y_pred=model.predict(X_test_scaled)
    accuracy=accuracy_score(y_test,y_pred)
    train_accuracy = model.score(X_train_scaled, y_train)
    test_accuracy = model.score(X_test_scaled, y_test)
    print("Training Accuracy of Random Forest Classifier:", train_accuracy)
    print("Test Accuracy of Random Forest Classifier:", test_accuracy,'\n')
    
def Support_Vector_Machine(X_train_scaled,y_train,X_test_scaled, y_test):
    model = SVC(kernel='rbf', gamma='scale')
    model.fit(X_train_scaled, y_train)
    y_pred=model.predict(X_test_scaled)
    accuracy=accuracy_score(y_test,y_pred)
    train_accuracy = model.score(X_train_scaled, y_train)
    test_accuracy = model.score(X_test_scaled, y_test)
    print("Training Accuracy of Support Vector Machine:", train_accuracy)
    print("Test Accuracy of Support Vector Machine:", test_accuracy)
    
    '''
    Performing Logistic Regression:

    Once the model is trained, you use it to predict the labels for the test set (X_test_scaled). These predicted labels (y_pred) are then compared with the actual labels in the test set (y_test). The accuracy of the model is calculated by comparing the predicted labels with the true labels in the test set using the accuracy_score function.

    To clarify:

    The model is trained using the training data (X_train_scaled and y_train).
    The trained model is then used to predict labels for the test data (X_test_scaled).
    Finally, the accuracy of the model is calculated by comparing the predicted labels with the actual labels in the test set (y_test).
    The accuracy score represents the proportion of correctly classified samples in the test set. It provides an estimate of how well the model generalizes to unseen data.
    
    3 modes: 
    
    1. hold, buy, sell , if 
    '''

'''
You're correct that the stock symbol itself may not inherently contain important information for predicting stock behavior. However, encoding the stock symbol can indirectly capture certain characteristics of the stock that might be relevant for prediction. Here's how encoding the stock symbol can potentially add value:

Market Sector Information: While the stock symbol is just a unique identifier for a particular stock, it often corresponds to the company's name or ticker symbol. This ticker symbol can indirectly convey information about the sector or industry to which the company belongs. Different sectors may exhibit different market behaviors, and encoding the sector information could help the model differentiate between stocks from different sectors.

Historical Performance: Some stocks may have historical performance trends that are specific to the company or industry. By encoding the stock symbol, the model can potentially learn from these historical patterns and incorporate them into its predictions.

Interactions with Other Features: The stock symbol may interact with other features in the dataset to influence the prediction outcome. For example, certain technical indicators or financial metrics may have different effects on different stocks based on their industry or market sector. By including the stock symbol as a feature, the model can learn these interactions and make more nuanced predictions.

Accounting for Unobserved Factors: There may be unobserved factors or characteristics associated with specific stocks that are not explicitly captured by other features in the dataset. Encoding the stock symbol allows the model to capture these unobserved factors indirectly, leading to potentially better predictions.

Overall, while the stock symbol itself may not directly contain predictive information, encoding it as a feature can help the model leverage underlying patterns or characteristics associated with different stocks to improve prediction accuracy. It's essential to evaluate the impact of including the stock symbol feature empirically through model performance metrics and validation techniques.

'''
    # do other classification models such as Random Forest Calssfier, Support Vector Machines (SVM), Gradient Boosting Classifier (XGBoost, LightGBM, or CatBoost)
    # change up classification, instead of buy, sell and hold, could do rise, fall, stay the same