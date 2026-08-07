import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("placement_data.csv")

X = data.drop("placed", axis=1)
y = data["placed"]

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "placement_model.pkl")

print("Model trained and saved successfully!")