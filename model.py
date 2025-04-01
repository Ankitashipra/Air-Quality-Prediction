import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
import seaborn as sns

# Load the dataset using openpyxl
df = pd.read_excel('C:/Users/KIIT/ad project/air+quality/AirQualityUCI.xlsx', engine='openpyxl')

# Handle missing values
df.replace(-200, np.nan, inplace=True)
df.dropna(inplace=True)

# Feature and target selection
features = ['CO(GT)', 'PT08.S1(CO)', 'C6H6(GT)', 'NOx(GT)', 'T', 'RH']
target = 'NO2(GT)'

X = df[features]
y = df[target]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Evaluate Train and Test Scores
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"Training R² Score: {train_score:.2f}")
print(f"Testing R² Score: {test_score:.2f}")

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R² Score: {r2:.2f}")

# Save the model
import joblib
joblib.dump(model, 'random_forest_model.pkl')
print("Model saved as 'random_forest_model.pkl'.")

# Visualizations

# 1. Actual vs Predicted Plot
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.5)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.xlabel('Actual NO2 (GT)')
plt.ylabel('Predicted NO2 (GT)')
plt.title('Actual vs Predicted NO2 Concentration')
plt.grid(True)
plt.show()

# 2. Residual Plot
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='purple')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Residuals Distribution')
plt.grid(True)
plt.show()

cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print("Cross-Validation R² Scores:", cv_scores)
print(f"Mean R² Score: {cv_scores.mean():.2f}")


sns.histplot(y_pred, color='green', kde=True)
plt.title("Distribution of Predicted AQI Values")
plt.show()

# 3. Feature Importance Plot
feature_importance = pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_})
feature_importance = feature_importance.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(8, 6))
sns.barplot(x='Importance', y='Feature', hue='Feature', data=feature_importance, palette='viridis', legend=False)

plt.title('Feature Importance Plot')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.grid(True)
plt.show()
