"""
Hotel Booking Demand - Model Training

This script trains machine learning models to predict hotel booking cancellations.

Goal: Build and compare models for cancellation prediction
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("HOTEL BOOKING DEMAND - MODEL TRAINING")
print("=" * 70)

# Import Libraries
print("\n1. Importing libraries...")
print("✓ Libraries imported successfully!")

# Load Prepared Data
print("\n2. Loading prepared data...")
# Load training and test data
X_train = pd.read_csv('data/X_train.csv')
X_test = pd.read_csv('data/X_test.csv')
y_train = pd.read_csv('data/y_train.csv')['is_canceled']
y_test = pd.read_csv('data/y_test.csv')['is_canceled']

print("✓ Data loaded successfully!")
print("=" * 50)
print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
print(f"Number of features: {X_train.shape[1]}")
print(f"\nCancellation rate in training: {y_train.mean()*100:.2f}%")
print(f"Cancellation rate in test: {y_test.mean()*100:.2f}%")

# Handle Any Remaining Missing Values
print("\n3. Handling any remaining missing values...")
# Check for missing values
print("Checking for missing values...")
print(f"X_train NaN count: {X_train.isnull().sum().sum()}")
print(f"X_test NaN count: {X_test.isnull().sum().sum()}")

# Fill any remaining NaN values with 0 (safe for scaled data)
if X_train.isnull().sum().sum() > 0 or X_test.isnull().sum().sum() > 0:
    print("\n⚠️  Found NaN values - filling with 0")
    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)
    print("✓ NaN values handled")
else:
    print("✓ No missing values found")

# Train Logistic Regression Model
print("\n4. Training Logistic Regression model...")
# Train Logistic Regression
print("Training Logistic Regression...")
lr_model = LogisticRegression(max_iter=1000, random_state=42, class_weight='balanced')
lr_model.fit(X_train, y_train)
print("✓ Logistic Regression trained")

# Evaluate Logistic Regression
print("\n5. Evaluating Logistic Regression...")
# Make predictions
lr_train_pred = lr_model.predict(X_train)
lr_test_pred = lr_model.predict(X_test)

# Calculate metrics
lr_metrics = {
    'model': 'Logistic Regression',
    'train_accuracy': accuracy_score(y_train, lr_train_pred),
    'test_accuracy': accuracy_score(y_test, lr_test_pred),
    'test_precision': precision_score(y_test, lr_test_pred),
    'test_recall': recall_score(y_test, lr_test_pred),
    'test_f1': f1_score(y_test, lr_test_pred)
}

print("Logistic Regression Results:")
print("=" * 50)
print(f"Training Accuracy: {lr_metrics['train_accuracy']:.4f}")
print(f"Test Accuracy: {lr_metrics['test_accuracy']:.4f}")
print(f"Test Precision: {lr_metrics['test_precision']:.4f}")
print(f"Test Recall: {lr_metrics['test_recall']:.4f}")
print(f"Test F1-Score: {lr_metrics['test_f1']:.4f}")

# Train Random Forest Model
print("\n6. Training Random Forest model...")
# Train Random Forest
print("Training Random Forest...")
rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42,
    class_weight='balanced',
    n_jobs=-1
)
rf_model.fit(X_train, y_train)
print("✓ Random Forest trained")

# Evaluate Random Forest
print("\n7. Evaluating Random Forest...")
# Make predictions
rf_train_pred = rf_model.predict(X_train)
rf_test_pred = rf_model.predict(X_test)

# Calculate metrics
rf_metrics = {
    'model': 'Random Forest',
    'train_accuracy': accuracy_score(y_train, rf_train_pred),
    'test_accuracy': accuracy_score(y_test, rf_test_pred),
    'test_precision': precision_score(y_test, rf_test_pred),
    'test_recall': recall_score(y_test, rf_test_pred),
    'test_f1': f1_score(y_test, rf_test_pred)
}

print("Random Forest Results:")
print("=" * 50)
print(f"Training Accuracy: {rf_metrics['train_accuracy']:.4f}")
print(f"Test Accuracy: {rf_metrics['test_accuracy']:.4f}")
print(f"Test Precision: {rf_metrics['test_precision']:.4f}")
print(f"Test Recall: {rf_metrics['test_recall']:.4f}")
print(f"Test F1-Score: {rf_metrics['test_f1']:.4f}")

# Compare Models
print("\n8. Comparing models...")
# Create comparison DataFrame
comparison_df = pd.DataFrame([lr_metrics, rf_metrics])
comparison_df = comparison_df.set_index('model')

print("Model Comparison:")
print("=" * 50)
print(comparison_df.round(4))

# Determine best model based on F1 score
best_model_name = comparison_df['test_f1'].idxmax()
print(f"\n✓ Best model: {best_model_name}")
print(f"  (based on Test F1-Score)")

# Feature Importance (Random Forest)
print("\n9. Analyzing feature importance (Random Forest)...")
# Get feature importance
feature_names = joblib.load('artifacts/feature_names.joblib')
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

print("Top 15 Most Important Features:")
print("=" * 50)
print(importance_df.head(15).to_string(index=False))

# Save Models and Metrics
print("\n10. Saving models and metrics...")
# Save models
joblib.dump(lr_model, 'artifacts/lr_model.joblib')
joblib.dump(rf_model, 'artifacts/rf_model.joblib')

# Save best model
if best_model_name == 'Random Forest':
    joblib.dump(rf_model, 'artifacts/best_model.joblib')
else:
    joblib.dump(lr_model, 'artifacts/best_model.joblib')

# Save metrics
comparison_df.to_csv('artifacts/model_metrics.csv')

# Save feature importance
importance_df.to_csv('artifacts/feature_importance.csv', index=False)

print("✓ Models and artifacts saved successfully!")
print("\nSaved files:")
print("  - artifacts/lr_model.joblib")
print("  - artifacts/rf_model.joblib")
print("  - artifacts/best_model.joblib")
print("  - artifacts/model_metrics.csv")
print("  - artifacts/feature_importance.csv")

print("\n" + "=" * 70)
print("MODEL TRAINING COMPLETE!")
print("=" * 70)
print(f"✓ Best model: {best_model_name}")
print(f"✓ Test Accuracy: {comparison_df.loc[best_model_name, 'test_accuracy']:.4f}")
print(f"✓ Test F1-Score: {comparison_df.loc[best_model_name, 'test_f1']:.4f}")
print("✓ Project complete!")
