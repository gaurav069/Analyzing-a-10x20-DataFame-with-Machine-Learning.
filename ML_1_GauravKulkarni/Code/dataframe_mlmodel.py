# -*- coding: utf-8 -*-
"""DataFrame_MLmodel.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C4nBlwADsHt2I2prEKMc8g-YskYGLvTs
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)
data = {
    "Age": np.random.randint(18, 80, size=20),
    "BMI": np.round(np.random.uniform(18.5, 40.0, size=20), 2),
    "BloodPressure": np.random.randint(80, 140, size=20),
    "Cholesterol": np.random.randint(150, 250, size=20),
    "Glucose": np.random.randint(70, 200, size=20),
    "Insulin": np.round(np.random.uniform(2.0, 50.0, size=20), 2),
    "SkinThickness": np.random.randint(5, 50, size=20),
    "FamilyHistory": np.random.choice([0, 1], size=20),
    "ExerciseLevel": np.random.choice(["Low", "Medium", "High"], size=20),
    "Diabetes": np.random.choice([0, 1], size=20),
}

df = pd.DataFrame(data)

df_encoded = pd.get_dummies(df, columns=["ExerciseLevel"], drop_first=True)

X = df_encoded.drop("Diabetes", axis=1)
y = df_encoded["Diabetes"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("DataFrame:")
print(df)
print("\nModel Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_rep)