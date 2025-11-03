"""
Hotel Booking Demand - Feature Engineering

This script creates features from the hotel booking dataset to prepare for machine learning.

Goal: Transform raw data into meaningful features for cancellation prediction
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("HOTEL BOOKING DEMAND - FEATURE ENGINEERING")
print("=" * 70)

# Import Libraries
print("\n1. Importing libraries...")
print("✓ Libraries imported successfully!")

# Load Data
print("\n2. Loading explored dataset...")
df = pd.read_csv('data/hotel_bookings_explored.csv')
print(f"✓ Dataset loaded: {df.shape}")
print(df.head())

# Handle Missing Values
print("\n3. Handling missing values...")
# Fill missing children with 0
if 'children' in df.columns:
    df['children'].fillna(0, inplace=True)

# Fill missing country with 'Unknown'
if 'country' in df.columns:
    df['country'].fillna('Unknown', inplace=True)

# Fill missing agent with 0
if 'agent' in df.columns:
    df['agent'].fillna(0, inplace=True)

# Fill missing company with 0
if 'company' in df.columns:
    df['company'].fillna(0, inplace=True)

print("✓ Missing values handled")
print(f"Remaining missing values: {df.isnull().sum().sum()}")

# Feature Engineering - Temporal Features
print("\n4. Creating temporal features...")
# Map months to numbers
month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['arrival_month_num'] = df['arrival_date_month'].map(month_map)

# Create season feature
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['arrival_month_num'].apply(get_season)

print("✓ Temporal features created")
print(f"  - arrival_month_num")
print(f"  - season")

# Feature Engineering - Booking Features
print("\n5. Creating booking features...")
# Total stay in nights (if not already created)
if 'total_nights' not in df.columns:
    df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

# Total guests (if not already created)
if 'total_guests' not in df.columns:
    df['total_guests'] = df['adults'] + df['children'] + df['babies']

# Has children flag
df['has_children'] = (df['children'] > 0).astype(int)

# Has babies flag
df['has_babies'] = (df['babies'] > 0).astype(int)

# Special requests flag
df['has_special_requests'] = (df['total_of_special_requests'] > 0).astype(int)

# Is repeated guest flag already exists in original data

print("✓ Booking features created")
print(f"  - total_nights: {df['total_nights'].mean():.2f} avg")
print(f"  - total_guests: {df['total_guests'].mean():.2f} avg")
print(f"  - has_children: {df['has_children'].sum()} bookings")
print(f"  - has_babies: {df['has_babies'].sum()} bookings")
print(f"  - has_special_requests: {df['has_special_requests'].sum()} bookings")

# Select Features for Modeling
print("\n6. Selecting features for modeling...")
# Select relevant features
feature_columns = [
    'hotel', 'lead_time', 'arrival_month_num', 'season',
    'stays_in_weekend_nights', 'stays_in_week_nights', 'total_nights',
    'adults', 'children', 'babies', 'total_guests',
    'meal', 'market_segment', 'distribution_channel',
    'is_repeated_guest', 'previous_cancellations',
    'previous_bookings_not_canceled', 'reserved_room_type',
    'assigned_room_type', 'booking_changes', 'deposit_type',
    'days_in_waiting_list', 'customer_type', 'adr',
    'required_car_parking_spaces', 'total_of_special_requests',
    'has_children', 'has_babies', 'has_special_requests'
]

# Keep only features that exist
feature_columns = [col for col in feature_columns if col in df.columns]

X = df[feature_columns].copy()
y = df['is_canceled'].copy()

print(f"✓ Selected {len(feature_columns)} features")
print(f"✓ Target variable: is_canceled")
print(f"✓ Dataset shape: {X.shape}")

# Encode Categorical Variables
print("\n7. Encoding categorical variables...")
# Identify categorical columns
categorical_cols = X.select_dtypes(include=['object']).columns.tolist()

print(f"Encoding {len(categorical_cols)} categorical columns:")
print(categorical_cols)

# Encode categorical variables
encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col].astype(str))
    encoders[col] = le

print(f"\n✓ All categorical variables encoded")
print(f"✓ Encoders saved: {len(encoders)}")

# Train-Test Split
print("\n8. Performing train-test split...")
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Train-Test Split:")
print("=" * 50)
print(f"Training set: {X_train.shape[0]} samples")
print(f"Test set: {X_test.shape[0]} samples")
print(f"\nTraining set cancellation rate: {y_train.mean()*100:.2f}%")
print(f"Test set cancellation rate: {y_test.mean()*100:.2f}%")

# Feature Scaling
print("\n9. Scaling features...")
# Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert back to DataFrame
X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns, index=X_test.index)

print("✓ Features scaled using StandardScaler")
print(f"✓ Training set shape: {X_train_scaled.shape}")
print(f"✓ Test set shape: {X_test_scaled.shape}")

# Save Processed Data and Artifacts
print("\n10. Saving processed data and artifacts...")
# Save datasets
X_train_scaled.to_csv('data/X_train.csv', index=False)
X_test_scaled.to_csv('data/X_test.csv', index=False)
y_train.to_csv('data/y_train.csv', index=False, header=True)
y_test.to_csv('data/y_test.csv', index=False, header=True)

# Save scaler and encoders
joblib.dump(scaler, 'artifacts/scaler.joblib')
joblib.dump(encoders, 'artifacts/encoders.joblib')

# Save feature names
feature_names = X_train.columns.tolist()
joblib.dump(feature_names, 'artifacts/feature_names.joblib')

print("✓ Data saved successfully!")
print("\nSaved files:")
print("  - data/X_train.csv")
print("  - data/X_test.csv")
print("  - data/y_train.csv")
print("  - data/y_test.csv")
print("  - artifacts/scaler.joblib")
print("  - artifacts/encoders.joblib")
print("  - artifacts/feature_names.joblib")

print("\n" + "=" * 70)
print("FEATURE ENGINEERING COMPLETE!")
print("=" * 70)
print(f"✓ Ready for model training with {len(feature_names)} features!")
