# 🏨 Hotel Booking Demand Project - Start Here!

Welcome! This guide will help you get started with the Hotel Booking Demand analysis project.

## 📥 Step 1: Get the Dataset

### Option A: Download from Kaggle (Recommended)
1. Go to https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
2. Click the **Download** button (you'll need a free Kaggle account)
3. Extract the ZIP file to get `hotel_bookings.csv`
4. Copy `hotel_bookings.csv` to the `data/` folder in this project

### Option B: Use Kaggle API
If you have Kaggle API credentials configured:
```bash
cd data
kaggle datasets download -d jessemostipak/hotel-booking-demand --unzip
```

## 🔧 Step 2: Install Dependencies

Open your terminal and run:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

Or if you prefer conda:
```bash
conda install pandas numpy scikit-learn matplotlib seaborn joblib -y
```

## 📚 Step 3: Run the Notebooks

Open the notebooks in order and execute all cells:

### 1️⃣ Data Exploration (`notebooks/01_data_exploration.ipynb`)
- Load and inspect the hotel booking dataset
- Analyze cancellation rates
- Explore seasonal patterns
- Understand guest demographics
- **Output**: Initial insights and cleaned dataset

### 2️⃣ Feature Engineering (`notebooks/02_feature_engineering.ipynb`)
- Create temporal features (season, day of week)
- Engineer booking-related features
- Encode categorical variables
- Split and scale data
- **Output**: Training and test datasets ready for modeling

### 3️⃣ Model Training (`notebooks/03_model_training.ipynb`)
- Train Logistic Regression and Random Forest models
- Compare model performance
- Evaluate using multiple metrics
- Save the best model
- **Output**: Trained models and performance metrics

## 🎯 What You'll Learn

- **Data Analysis**: How to explore hotel booking patterns
- **Feature Engineering**: Creating meaningful features from dates and categories
- **Machine Learning**: Building classification models for cancellation prediction
- **Model Evaluation**: Comparing models with appropriate metrics
- **Real-world Application**: Solving a practical business problem

## 📊 Dataset Overview

The Hotel Booking Demand dataset contains approximately **119,390 bookings** with features including:

- **Temporal**: Arrival date, booking date, lead time
- **Stay**: Number of nights (weekend/weekday)
- **Guests**: Adults, children, babies
- **Booking**: Hotel type, meal plan, market segment
- **Financial**: Average daily rate (ADR), deposit type
- **Target**: `is_canceled` (0 = not canceled, 1 = canceled)

## ⚠️ Common Issues

### "File not found" error
Make sure `hotel_bookings.csv` is in the `data/` folder.

### Import errors
Ensure all required packages are installed using pip or conda.

### Notebook kernel issues
Make sure you're using a Python 3.x kernel with all dependencies installed.

## 🎓 Project Difficulty

**Level**: Intermediate

**Skills Required**:
- Basic Python programming
- Understanding of pandas and numpy
- Familiarity with scikit-learn
- Basic machine learning concepts

**Time to Complete**: 2-3 hours

## 🚀 Next Steps

After completing the notebooks:
1. Try different models (XGBoost, LightGBM)
2. Perform hyperparameter tuning
3. Create a Streamlit demo app
4. Deploy the model as an API

## 💡 Tips

- Read the code comments carefully
- Try modifying parameters to see how results change
- Document your observations in markdown cells
- Experiment with different feature combinations

## 🤔 Need Help?

If you encounter issues:
1. Check that the dataset is in the correct location
2. Verify all dependencies are installed
3. Make sure you're running notebooks in order
4. Review error messages carefully

Happy analyzing! 🎉
