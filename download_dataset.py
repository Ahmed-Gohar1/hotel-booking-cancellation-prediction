"""
Download Hotel Booking Demand dataset using kagglehub
"""
import kagglehub
import shutil
import os

print("Downloading Hotel Booking Demand dataset...")
print("=" * 60)

# Download latest version
path = kagglehub.dataset_download("jessemostipak/hotel-booking-demand")

print(f"\n✓ Dataset downloaded to: {path}")

# Find the CSV file
csv_files = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.csv'):
            csv_files.append(os.path.join(root, file))

print(f"\n✓ Found {len(csv_files)} CSV file(s):")
for csv_file in csv_files:
    print(f"  - {csv_file}")

# Copy to project data folder
if csv_files:
    source_file = csv_files[0]
    dest_file = os.path.join(os.path.dirname(__file__), 'data', 'hotel_bookings.csv')
    
    shutil.copy2(source_file, dest_file)
    print(f"\n✓ Dataset copied to: {dest_file}")
    
    # Verify file size
    file_size = os.path.getsize(dest_file)
    file_size_mb = file_size / (1024 * 1024)
    print(f"✓ File size: {file_size_mb:.2f} MB")
    
    # Quick data check
    import pandas as pd
    df = pd.read_csv(dest_file)
    print(f"\n✓ Dataset loaded successfully!")
    print(f"  - Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"  - Columns: {list(df.columns)[:5]}... (showing first 5)")
    print(f"  - Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    
    print("\n" + "=" * 60)
    print("✅ Dataset ready for analysis!")
else:
    print("\n❌ No CSV files found in the downloaded dataset")
