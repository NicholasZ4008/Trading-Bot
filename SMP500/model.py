from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

def model_analysis():
    data = pd.read_csv('decisions.csv')
    data = data.dropna()

    X = pd.get_dummies(data.drop(columns=['decision', 'Date']))
    y = data['decision']

    X_train, X_valid, y_train, y_valid = train_test_split(X,y)

    rf_pipeline = make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=100))
    dt_pipeline = make_pipeline(StandardScaler(), DecisionTreeClassifier())
    nn_pipeline = make_pipeline(StandardScaler(), MLPClassifier(max_iter=1000))

    pipelines = [rf_pipeline, dt_pipeline, nn_pipeline]
    for pipeline in pipelines:
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_valid)
        print(f"Accuracy of {pipeline.steps[-1][1].__class__.__name__}: {accuracy_score(y_valid, y_pred):.2f}")
     


