import matplotlib.pyplot as plt
import pandas as pd
from fetch_data import get_player_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Fetch data and prep features
df = get_player_data()
df_features = df.drop(columns=['name'])
df_encoded = pd.get_dummies(df_features, columns=['position'], drop_first=True)

X = df_encoded.drop('value_m_euro', axis=1)
y = df_encoded['value_m_euro']

# Re-Train and make prediction on all of the data in the set for visualisation
model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)

# Plot results
plt.figure(figsize=(8,5))
plt.scatter(y, predictions, color='blue', s=100, label='Players (Guess vs Actual)')
plt.plot([0, 70], [0,70], color='red', linestyle='--', label = "Perfect Match (1:1)")

plt.xlabel('Actual Value (M EURO)')
plt.ylabel('Predicted Value (M EURO)')
plt.title('Transfer Value Predictor: Actual vs. Predicted Value')
plt.legend()
plt.grid(True, alpha=0.3)

# Show plot
plt.show()