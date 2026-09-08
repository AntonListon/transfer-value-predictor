# File to train future model for the project

# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from fetch_data import get_player_data

# Fetch the data from fetch_data.py
df = get_player_data()

# Dataprocessing
# Removes the name due to irrelevance and convert the positions into true/false variables (one-hot encoding)
df_features = df.drop(columns=['name'])
df_encoded = pd.get_dummies(df_features, columns=['position'], drop_first=True)

# Split the data into features(X) and target variable(y)
X = df_encoded.drop('value_m_euro', axis=1)
y = df_encoded['value_m_euro']

# 80% of the data is used for training and 20% for testing
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print("\n--- Model Trained Succesfully ---")
print(f"Mean Squared Error on test-data: {mse:.2f}")

# Test with a new dummy player based on the data in fetch_data.py
player = pd.DataFrame([{
    'age': 24,
    'minutes': 2000,
    'goals': 4,
    'assists': 6,
    'position_Forward': False,
    'position_Midfielder': True
}])

estimated_value = model.predict(player)
print(f"\nEstimated value of the player: {estimated_value[0]:.2f} million euros")