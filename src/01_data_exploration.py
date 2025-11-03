"""
Hotel Booking Demand - Data Exploration

This script explores the hotel booking dataset and creates initial features.

Goal: Understand the dataset and create basic features for further analysis
"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("HOTEL BOOKING DEMAND - DATA EXPLORATION")
print("=" * 70)

# Import Libraries
print("\n1. Importing libraries...")
print("✓ Libraries imported successfully!")

# Load Data
print("\n2. Loading dataset...")
df = pd.read_csv('../data/hotel_bookings.csv')
print(f"✓ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

# Basic Info
print("\n3. Dataset Overview:")
print("=" * 70)
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"Memory usage: {df.memory_usage().sum() / 1024**2:.2f} MB")

# Check Missing Values
print("\n4. Missing Values Analysis:")
print("=" * 70)
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({
    'Column': missing.index,
    'Missing Count': missing.values,
    'Percentage': missing_pct.values
})
missing_df = missing_df[missing_df['Missing Count'] > 0].sort_values('Missing Count', ascending=False)
if len(missing_df) > 0:
    print(missing_df.to_string(index=False))
else:
    print("✓ No missing values found!")

# Analyze Cancellations
print("\n5. Cancellation Analysis:")
print("=" * 70)
cancellation_rate = df['is_canceled'].mean() * 100
print(f"Overall cancellation rate: {cancellation_rate:.2f}%")
print(f"Total bookings: {len(df)}")
print(f"Canceled: {df['is_canceled'].sum()}")
print(f"Not canceled: {(df['is_canceled'] == 0).sum()}")

# Analyze Hotel Types
print("\n6. Hotel Types Analysis:")
print("=" * 70)
hotel_counts = df['hotel'].value_counts()
print(hotel_counts)
print(f"\nCancellation rate by hotel:")
for hotel in df['hotel'].unique():
    rate = df[df['hotel'] == hotel]['is_canceled'].mean() * 100
    print(f"  {hotel}: {rate:.2f}%")

# Analyze Guests
print("\n7. Guest Analysis:")
print("=" * 70)
print(f"Average adults per booking: {df['adults'].mean():.2f}")
print(f"Average children per booking: {df['children'].mean():.2f}")
print(f"Average babies per booking: {df['babies'].mean():.2f}")
total_guests = df['adults'] + df['children'].fillna(0) + df['babies']
print(f"Average total guests per booking: {total_guests.mean():.2f}")

# Analyze Temporal Patterns
print("\n8. Temporal Patterns:")
print("=" * 70)
print("Bookings by arrival month:")
print(df['arrival_date_month'].value_counts().sort_index())
print(f"\nBookings by year:")
print(df['arrival_date_year'].value_counts().sort_index())

# Analyze Stay Duration
print("\n9. Stay Duration Analysis:")
print("=" * 70)
print(f"Average weekend nights: {df['stays_in_weekend_nights'].mean():.2f}")
print(f"Average week nights: {df['stays_in_week_nights'].mean():.2f}")
total_nights = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
print(f"Average total nights: {total_nights.mean():.2f}")
print(f"Max total nights: {total_nights.max()}")

# Analyze Lead Time
print("\n10. Lead Time Analysis:")
print("=" * 70)
print(f"Average lead time: {df['lead_time'].mean():.2f} days")
print(f"Median lead time: {df['lead_time'].median():.2f} days")
print(f"Max lead time: {df['lead_time'].max()} days")

# Analyze ADR (Average Daily Rate)
print("\n11. ADR (Average Daily Rate) Analysis:")
print("=" * 70)
adr_data = df[df['adr'] > 0]['adr']
print(f"Average ADR: ${adr_data.mean():.2f}")
print(f"Median ADR: ${adr_data.median():.2f}")
print(f"Min ADR: ${adr_data.min():.2f}")
print(f"Max ADR: ${adr_data.max():.2f}")

# Analyze Market Segment
print("\n12. Market Segment Analysis:")
print("=" * 70)
print(df['market_segment'].value_counts())

# Create Additional Features
print("\n13. Creating Additional Features:")
print("=" * 70)
df['total_guests'] = df['adults'] + df['children'].fillna(0) + df['babies']
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']
print("✓ Created features:")
print(f"  - total_guests: Average {df['total_guests'].mean():.2f}")
print(f"  - total_nights: Average {df['total_nights'].mean():.2f}")

# Save Explored Data
print("\n14. Saving explored data...")
df.to_csv('data/hotel_bookings_explored.csv', index=False)
print("✓ Data saved to: data/hotel_bookings_explored.csv")

print("\n" + "=" * 70)
print("DATA EXPLORATION COMPLETE!")
print("=" * 70)
print(f"✓ Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"✓ Cancellation rate: {cancellation_rate:.2f}%")
print(f"✓ Average guests: {df['total_guests'].mean():.2f}")
print(f"✓ Average nights: {df['total_nights'].mean():.2f}")
print("✓ Ready for feature engineering!")
