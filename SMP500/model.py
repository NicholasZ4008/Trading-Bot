from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

# Uncomment MLP to test out MLPClassifier model

def model_analysis(use_only_dtc=False):
    data = pd.read_csv('decisions.csv').dropna()

    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)

    # Drop other non-feature columns
    X = data.drop(columns=['decision', 'Date', 'Symbol'])
    y = data['decision']
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.25)
    pipelines = {
        "RandomForest": make_pipeline(StandardScaler(), RandomForestClassifier(n_estimators=100)),
        "DecisionTree": make_pipeline(StandardScaler(), DecisionTreeClassifier()),
        # "MLP": make_pipeline(StandardScaler(), MLPClassifier(max_iter=1000))
    }
    for name, pipeline in pipelines.items():
        if use_only_dtc and name != "DecisionTree":
            continue
        pipeline.fit(X_train, y_train)
        train_score = pipeline.score(X_train, y_train)
        valid_score = pipeline.score(X_valid, y_valid)
        if not use_only_dtc:
            print(f"Train Score of {name}: {train_score}\n")
            print(f"Test Score of {name}: {valid_score}\n")

    # Return the specified model or all models
    if use_only_dtc:
        return pipelines["DecisionTree"]
    return pipelines


