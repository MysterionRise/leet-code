import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
import numpy as np


train_df = pd.read_csv("train.csv")  # columns: ["body", "label"]
print("Train shape:", train_df.shape)

# Optional: quick check
# display(train_df.head())

# Split into features (X) and labels (y)
X = train_df["body"]
y = train_df["label"]

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a pipeline: TF-IDF then LogisticRegression
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression(solver='liblinear', random_state=42))
])

# Train the pipeline
pipeline.fit(X_train, y_train)

# Predict on validation split
y_pred_val = pipeline.predict(X_val)

# Calculate accuracy
val_acc = accuracy_score(y_val, y_pred_val)
print("Validation Accuracy:", val_acc)

# 3.1: Re-train on the entire train.csv for best performance
pipeline.fit(X, y)

# 3.2: Read test.csv
test_df = pd.read_csv("test.csv")  # single column: ["body"]
X_test = test_df["body"]

# 3.3: Predict on the test set
y_test_pred = pipeline.predict(X_test)

# Convert numerical predictions to strings
pred_strings = [str(p) for p in y_test_pred]

# Join them with a space
pred_output_str = " ".join(pred_strings)

# Write to file
with open("predictions.txt", "w") as f:
    f.write(pred_output_str)

print("Predictions saved to predictions.txt")
