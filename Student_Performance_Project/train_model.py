import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Student_Performance.csv')
print(df.head())
print(df.info())
print(df.isnull().sum().sum())
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
categorical_cols = df.select_dtypes(include=['object']).columns
print("Numerical Columns:", numerical_cols)
print("Categorical Columns:", categorical_cols)
plt.figure(figsize=(12, 8))
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Feature Correlation Matrix')
plt.tight_layout()
plt.show()
for col in categorical_cols:
    plt.figure(figsize=(10, 4))
    sns.boxplot(x=col, y='overall_score', data=df)
    plt.title(f'Overall Score vs {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
X = df[['study_hours', 'math_score', 'science_score', 'english_score',
        'parent_education', 'travel_time', 
         'study_method']]
y = df['overall_score']

categorical_columns = ['parent_education', 'travel_time', 'study_method']
numeric_columns = ['study_hours', 'math_score', 'science_score', 'english_score']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_columns), 
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_columns) 
    ])

X_processed = preprocessor.fit_transform(X)

# 6. Checking new feature shape
print(f"Original features: {X.shape[1]}")
print(f"Encoded features: {X_processed.shape[1]}")
print(f"New feature names: \n{preprocessor.get_feature_names_out()}")
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

# 7. Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X_processed, y, test_size=0.2, random_state=42
)

# 8. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 9. Make predictions
y_pred = model.predict(X_test)
y_train_pred = model.predict(X_train)

# 10. Evaluate model
r2_test = r2_score(y_test, y_pred)
r2_train = r2_score(y_train, y_train_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nModel Performance:")
print(f"Train R² Score: {r2_train:.4f} ({r2_train*100:.2f}%)")
print(f"Test R² Score: {r2_test:.4f} ({r2_test*100:.2f}%)")
print(f"Mean Absolute Error: {mae:.2f} points")
print(f"Root Mean Squared Error: {rmse:.2f} points")

overfit_gap = r2_train - r2_test
print(f"\nOverfitting Check:")
if overfit_gap < 0.02:
    print(f"No overfitting (Difference: {overfit_gap:.4f})")
else:
    print(f"Possible overfitting (Difference: {overfit_gap:.4f})")

# 12. Feature importance
feature_names = preprocessor.get_feature_names_out()
coefficients = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': model.coef_
}).sort_values('Coefficient', ascending=False)

print("\n Top 5 Most Important Features:")
print(coefficients.head(5))
print("\n Bottom 5 Least Important Features:")
print(coefficients.tail(5))

import matplotlib.pyplot as plt
import numpy as np

# Actual vs Predicted Graph
plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.6, color='blue', edgecolors='black', linewidth=0.5)

# Perfect prediction line (y = x)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='Perfect Prediction (y=x)')

plt.xlabel('Actual Overall Score', fontsize=12)
plt.ylabel('Predicted Overall Score', fontsize=12)
plt.title(f'Actual vs Predicted Overall Score\nR² = {r2_test:.4f} ({r2_test*100:.2f}%)', fontsize=14)

plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
import joblib

# Save model and preprocessor
joblib.dump(model, 'student_performance_model.pkl')
joblib.dump(preprocessor, 'preprocessor.pkl')

print("Model and preprocessor saved successfully!")

