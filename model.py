import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv("house_data.csv")

# Optional: clean column names (remove spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# Features and target
X = df[["area", "bedrooms", "bathrooms"]]
y = df["price"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained and saved successfully")
