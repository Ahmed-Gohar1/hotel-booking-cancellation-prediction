"""
Simple Hotel Booking EDA - Visualization Script

This script performs exploratory data analysis on hotel booking data
and saves all visualizations to the reports/figures folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Get absolute paths for data and output directories
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
output_dir = os.path.join(project_dir, 'reports', 'figures')
os.makedirs(output_dir, exist_ok=True)

print("=" * 70)
print("HOTEL BOOKING EDA - GENERATING VISUALIZATIONS")
print("=" * 70)

# 1. Import Libraries & Load Data
print("\n1. Loading data...")
# Get the absolute path to the data file
data_path = os.path.join(project_dir, 'data', 'hotel_bookings.csv')
df = pd.read_csv(data_path)
print(f"✓ Dataset has {len(df):,} bookings")
print(f"✓ Cancellation rate: {df['is_canceled'].mean()*100:.1f}%")

# 2. Cancellation Overview
print("\n2. Generating cancellation overview...")
plt.figure(figsize=(8, 6))
cancel_counts = df['is_canceled'].value_counts()
plt.pie(cancel_counts, labels=['Not Canceled', 'Canceled'], autopct='%1.1f%%', 
        colors=['green', 'red'], startangle=90)
plt.title('Booking Cancellations', size=14, weight='bold')
plt.savefig(f'{output_dir}/01_cancellation_overview.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 01_cancellation_overview.png")

# 3. Hotel Types
print("\n3. Generating hotel types analysis...")
hotel_data = df.groupby('hotel')['is_canceled'].mean() * 100

plt.figure(figsize=(8, 5))
hotel_data.plot(kind='bar', color=['skyblue', 'coral'])
plt.title('Cancellation Rate by Hotel Type', size=14, weight='bold')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f'{output_dir}/02_hotel_types.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 02_hotel_types.png")

# 4. Booking Trends by Month
print("\n4. Generating monthly booking trends...")
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
month_counts = df['arrival_date_month'].value_counts().reindex(month_order)

plt.figure(figsize=(12, 5))
plt.plot(month_order, month_counts.values, marker='o', linewidth=2, color='blue')
plt.title('Bookings by Month', size=14, weight='bold')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f'{output_dir}/03_monthly_trends.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 03_monthly_trends.png")

# 5. Lead Time Analysis
print("\n5. Generating lead time analysis...")
plt.figure(figsize=(10, 5))
plt.hist(df[df['is_canceled']==0]['lead_time'], bins=50, alpha=0.6, label='Not Canceled', color='green')
plt.hist(df[df['is_canceled']==1]['lead_time'], bins=50, alpha=0.6, label='Canceled', color='red')
plt.title('Lead Time: Canceled vs Not Canceled', size=14, weight='bold')
plt.xlabel('Lead Time (days)')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig(f'{output_dir}/04_lead_time.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 04_lead_time.png")

# 6. Market Segments
print("\n6. Generating market segments analysis...")
top_segments = df['market_segment'].value_counts().head(5)

plt.figure(figsize=(10, 5))
top_segments.plot(kind='barh', color='teal')
plt.title('Top 5 Market Segments', size=14, weight='bold')
plt.xlabel('Number of Bookings')
plt.tight_layout()
plt.savefig(f'{output_dir}/05_market_segments.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 05_market_segments.png")

# 7. Average Daily Rate (ADR)
print("\n7. Generating ADR distribution...")
adr_data = df[df['adr'] > 0]['adr']

plt.figure(figsize=(10, 5))
plt.hist(adr_data, bins=50, color='gold', edgecolor='black')
plt.title('Average Daily Rate Distribution', size=14, weight='bold')
plt.xlabel('ADR ($)')
plt.ylabel('Count')
plt.axvline(adr_data.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${adr_data.mean():.2f}')
plt.legend()
plt.tight_layout()
plt.savefig(f'{output_dir}/06_adr_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 06_adr_distribution.png")

# 8. Key Correlations
print("\n8. Generating correlation analysis...")
numerical_cols = ['lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights',
                  'adults', 'children', 'babies', 'is_repeated_guest',
                  'previous_cancellations', 'booking_changes', 'adr',
                  'total_of_special_requests']

corr_data = df[numerical_cols + ['is_canceled']].corr()['is_canceled'].drop('is_canceled').sort_values()

plt.figure(figsize=(10, 6))
corr_data.plot(kind='barh', color=['red' if x < 0 else 'green' for x in corr_data])
plt.title('Correlation with Cancellation', size=14, weight='bold')
plt.xlabel('Correlation')
plt.axvline(0, color='black', linewidth=0.8)
plt.tight_layout()
plt.savefig(f'{output_dir}/07_correlations.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 07_correlations.png")

# 9. Guest Patterns
print("\n9. Generating guest patterns...")
df['total_guests'] = df['adults'] + df['children'].fillna(0) + df['babies']

plt.figure(figsize=(10, 5))
plt.hist(df['total_guests'], bins=15, color='purple', edgecolor='black')
plt.title('Number of Guests per Booking', size=14, weight='bold')
plt.xlabel('Total Guests')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(f'{output_dir}/08_guest_patterns.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 08_guest_patterns.png")

# 10. Stay Duration
print("\n10. Generating stay duration analysis...")
df['total_nights'] = df['stays_in_weekend_nights'] + df['stays_in_week_nights']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Total nights histogram
axes[0].hist(df['total_nights'], bins=30, color='orange', edgecolor='black')
axes[0].set_title('Stay Duration Distribution', size=14, weight='bold')
axes[0].set_xlabel('Total Nights')
axes[0].set_ylabel('Count')

# Weekend vs weekday
stay_data = pd.DataFrame({
    'Weekend Nights': [df['stays_in_weekend_nights'].sum()],
    'Week Nights': [df['stays_in_week_nights'].sum()]
})
stay_data.T.plot(kind='bar', ax=axes[1], color=['skyblue', 'coral'], legend=False)
axes[1].set_title('Weekend vs Weekday Stays', size=14, weight='bold')
axes[1].set_ylabel('Total Nights')
axes[1].set_xticklabels(['Weekend', 'Weekday'], rotation=0)

plt.tight_layout()
plt.savefig(f'{output_dir}/09_stay_duration.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 09_stay_duration.png")

# 11. Customer Types
print("\n11. Generating customer types analysis...")
customer_counts = df['customer_type'].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
axes[0].bar(customer_counts.index, customer_counts.values, color='steelblue')
axes[0].set_title('Bookings by Customer Type', size=14, weight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Cancellation rate
customer_cancel = df.groupby('customer_type')['is_canceled'].mean() * 100
axes[1].bar(customer_cancel.index, customer_cancel.values, color='crimson')
axes[1].set_title('Cancellation Rate by Customer Type', size=14, weight='bold')
axes[1].set_ylabel('Cancellation Rate (%)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(f'{output_dir}/10_customer_types.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 10_customer_types.png")

# 12. Deposit Type Impact
print("\n12. Generating deposit type analysis...")
deposit_cancel = df.groupby('deposit_type')['is_canceled'].mean() * 100

plt.figure(figsize=(10, 5))
deposit_cancel.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('Cancellation Rate by Deposit Type', size=14, weight='bold')
plt.ylabel('Cancellation Rate (%)')
plt.xlabel('Deposit Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'{output_dir}/11_deposit_type.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 11_deposit_type.png")

# 13. Meal Preferences
print("\n13. Generating meal preferences...")
meal_counts = df['meal'].value_counts()

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Bar chart
axes[0].bar(meal_counts.index, meal_counts.values, color='teal')
axes[0].set_title('Bookings by Meal Type', size=14, weight='bold')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Pie chart
axes[1].pie(meal_counts.values, labels=meal_counts.index, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Meal Type Distribution', size=14, weight='bold')

plt.tight_layout()
plt.savefig(f'{output_dir}/12_meal_preferences.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 12_meal_preferences.png")

# 14. Special Requests
print("\n14. Generating special requests analysis...")
plt.figure(figsize=(10, 5))
plt.hist(df['total_of_special_requests'], bins=10, color='gold', edgecolor='black')
plt.title('Special Requests Distribution', size=14, weight='bold')
plt.xlabel('Number of Special Requests')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(f'{output_dir}/13_special_requests.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 13_special_requests.png")

# 15. Repeated Guests
print("\n15. Generating repeated guests analysis...")
repeated_data = df['is_repeated_guest'].value_counts()
repeated_labels = ['New Guest', 'Repeated Guest']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Count
axes[0].bar(repeated_labels, repeated_data.values, color=['blue', 'green'])
axes[0].set_title('New vs Repeated Guests', size=14, weight='bold')
axes[0].set_ylabel('Count')

# Cancellation comparison
cancel_new = df[df['is_repeated_guest']==0]['is_canceled'].mean() * 100
cancel_repeated = df[df['is_repeated_guest']==1]['is_canceled'].mean() * 100
axes[1].bar(repeated_labels, [cancel_new, cancel_repeated], color=['orange', 'red'])
axes[1].set_title('Cancellation Rate: New vs Repeated', size=14, weight='bold')
axes[1].set_ylabel('Cancellation Rate (%)')

plt.tight_layout()
plt.savefig(f'{output_dir}/14_repeated_guests.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 14_repeated_guests.png")

# 16. Booking Changes
print("\n16. Generating booking changes analysis...")
plt.figure(figsize=(10, 5))
plt.hist(df['booking_changes'], bins=15, color='purple', edgecolor='black')
plt.title('Booking Changes Distribution', size=14, weight='bold')
plt.xlabel('Number of Changes')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(f'{output_dir}/15_booking_changes.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 15_booking_changes.png")

# 17. Arrival Year Trends
print("\n17. Generating year trends...")
year_data = df.groupby('arrival_date_year').agg({
    'is_canceled': ['count', 'sum', 'mean']
}).reset_index()
year_data.columns = ['Year', 'Total', 'Canceled', 'Cancel_Rate']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Total bookings
axes[0].bar(year_data['Year'], year_data['Total'], color='skyblue')
axes[0].set_title('Total Bookings by Year', size=14, weight='bold')
axes[0].set_ylabel('Number of Bookings')
axes[0].set_xlabel('Year')

# Cancellation rate
axes[1].plot(year_data['Year'], year_data['Cancel_Rate']*100, marker='o', linewidth=2, color='red', markersize=10)
axes[1].set_title('Cancellation Rate by Year', size=14, weight='bold')
axes[1].set_ylabel('Cancellation Rate (%)')
axes[1].set_xlabel('Year')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{output_dir}/16_year_trends.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 16_year_trends.png")

# 18. Distribution Channels
print("\n18. Generating distribution channels...")
channel_counts = df['distribution_channel'].value_counts()

plt.figure(figsize=(10, 5))
channel_counts.plot(kind='barh', color='teal')
plt.title('Bookings by Distribution Channel', size=14, weight='bold')
plt.xlabel('Number of Bookings')
plt.ylabel('Channel')
plt.tight_layout()
plt.savefig(f'{output_dir}/17_distribution_channels.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 17_distribution_channels.png")

# 19. Previous Cancellations
print("\n19. Generating previous cancellations analysis...")
has_previous = df[df['previous_cancellations'] > 0]

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Distribution
axes[0].hist(df['previous_cancellations'], bins=20, color='crimson', edgecolor='black')
axes[0].set_title('Previous Cancellations Distribution', size=14, weight='bold')
axes[0].set_xlabel('Previous Cancellations')
axes[0].set_ylabel('Count')

# Impact on current cancellation
cancel_with_history = has_previous['is_canceled'].mean() * 100
cancel_no_history = df[df['previous_cancellations']==0]['is_canceled'].mean() * 100
axes[1].bar(['No History', 'Has History'], [cancel_no_history, cancel_with_history], 
            color=['green', 'red'])
axes[1].set_title('Cancellation: With vs Without History', size=14, weight='bold')
axes[1].set_ylabel('Cancellation Rate (%)')

plt.tight_layout()
plt.savefig(f'{output_dir}/18_previous_cancellations.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 18_previous_cancellations.png")

# 20. ADR vs Cancellation
print("\n20. Generating ADR comparison...")
adr_not_canceled = df[(df['is_canceled']==0) & (df['adr']>0) & (df['adr']<500)]['adr']
adr_canceled = df[(df['is_canceled']==1) & (df['adr']>0) & (df['adr']<500)]['adr']

plt.figure(figsize=(10, 5))
plt.hist(adr_not_canceled, bins=50, alpha=0.6, label='Not Canceled', color='green')
plt.hist(adr_canceled, bins=50, alpha=0.6, label='Canceled', color='red')
plt.title('ADR: Canceled vs Not Canceled', size=14, weight='bold')
plt.xlabel('ADR ($)')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig(f'{output_dir}/19_adr_comparison.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 19_adr_comparison.png")

# 21. Parking Spaces
print("\n21. Generating parking spaces analysis...")
parking_counts = df['required_car_parking_spaces'].value_counts().sort_index()

plt.figure(figsize=(10, 5))
parking_counts.plot(kind='bar', color='steelblue')
plt.title('Parking Space Requirements', size=14, weight='bold')
plt.xlabel('Number of Parking Spaces')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f'{output_dir}/20_parking_spaces.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"✓ Saved: 20_parking_spaces.png")

# Summary
print("\n" + "=" * 70)
print("KEY INSIGHTS SUMMARY")
print("=" * 70)

print(f"\n1. Total Bookings: {len(df):,}")
print(f"2. Cancellation Rate: {df['is_canceled'].mean()*100:.1f}%")
print(f"3. Average Lead Time: {df['lead_time'].mean():.0f} days")
print(f"4. Average Price (ADR): ${df[df['adr']>0]['adr'].mean():.2f}")
print(f"5. Average Guests: {df['total_guests'].mean():.2f}")
print(f"6. Average Stay: {df['total_nights'].mean():.2f} nights")
print(f"7. Most Canceled Month: {df[df['is_canceled']==1]['arrival_date_month'].value_counts().index[0]}")
print(f"8. Busiest Month: {df['arrival_date_month'].value_counts().index[0]}")
print(f"9. Repeated Guests: {(df['is_repeated_guest']==1).mean()*100:.1f}%")

with_requests = df[df['total_of_special_requests'] > 0]['is_canceled'].mean() * 100
without_requests = df[df['total_of_special_requests'] == 0]['is_canceled'].mean() * 100
print(f"10. Special Requests Impact:")
print(f"    - With requests: {with_requests:.1f}% cancellation")
print(f"    - Without requests: {without_requests:.1f}% cancellation")

print("\n" + "=" * 70)
print(f"✓ ALL VISUALIZATIONS SAVED TO: {output_dir}/")
print(f"✓ Total: 20 visualization files created")
print("=" * 70)
