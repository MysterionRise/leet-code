import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import numpy as np


train_df = pd.read_csv("train.csv") 

X = train_df["body"]
y = train_df["label"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(solver='liblinear', random_state=42))
])

pipeline.fit(X_train, y_train)

y_pred_val = pipeline.predict(X_val)

val_acc = accuracy_score(y_val, y_pred_val)
print("acc:", val_acc)

pipeline.fit(X, y)

test_df = pd.read_csv("test.csv")  
X_test = test_df["body"]

y_test_pred = pipeline.predict(X_test)

pred_strings = [str(p) for p in y_test_pred]

pred_output_str = " ".join(pred_strings)

with open("predictions.txt", "w") as f:
    f.write(pred_output_str)
