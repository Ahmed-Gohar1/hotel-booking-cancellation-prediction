# Hotel Booking Demand - Notebooks

This folder contains Jupyter notebooks for analyzing and predicting hotel booking cancellations.

## 📚 Notebook Order

Run the notebooks in this order:

### 1. `01_data_exploration.ipynb`
**Purpose**: Explore and understand the hotel booking dataset

**What it does**:
- Loads the hotel_bookings.csv dataset
- Analyzes cancellation rates (target variable)
- Explores hotel types (City vs Resort)
- Analyzes guest composition
- Studies temporal patterns (months, years)
- Examines stay duration and lead time
- Analyzes pricing (ADR) patterns
- Studies market segments

**Outputs**:
- `data/hotel_bookings_explored.csv` - Dataset with additional features

**Key Insights**:
- Overall cancellation rate
- Differences between city and resort hotels
- Seasonal booking patterns
- Guest demographics

---

### 2. `02_feature_engineering.ipynb`
**Purpose**: Transform raw data into features for machine learning

**What it does**:
- Handles missing values
- Creates temporal features (month numbers, seasons)
- Engineers booking features (total nights, total guests)
- Creates binary flags (has_children, has_babies, etc.)
- Encodes categorical variables
- Splits data into training and test sets (80/20)
- Scales features using StandardScaler

**Outputs**:
- `data/X_train.csv` - Training features
- `data/X_test.csv` - Test features
- `data/y_train.csv` - Training labels
- `data/y_test.csv` - Test labels
- `artifacts/scaler.joblib` - Fitted scaler
- `artifacts/encoders.joblib` - Label encoders
- `artifacts/feature_names.joblib` - Feature names

**Features Created**:
- 27+ engineered features
- Temporal, booking, and guest features
- All categorical variables encoded

---

### 3. `03_model_training.ipynb`
**Purpose**: Train and compare machine learning models

**What it does**:
- Loads prepared training and test data
- Trains Logistic Regression (baseline)
- Trains Random Forest Classifier
- Evaluates both models on multiple metrics
- Compares model performance
- Analyzes feature importance
- Saves the best model

**Outputs**:
- `artifacts/lr_model.joblib` - Logistic Regression model
- `artifacts/rf_model.joblib` - Random Forest model
- `artifacts/best_model.joblib` - Best performing model
- `artifacts/model_metrics.csv` - Performance comparison
- `artifacts/feature_importance.csv` - Feature rankings

**Metrics Evaluated**:
- Accuracy
- Precision
- Recall
- F1-Score

---

## 🚀 Quick Start

1. **Download the dataset**: Place `hotel_bookings.csv` in the `../data/` folder
2. **Run notebook 1**: Explore the data
3. **Run notebook 2**: Engineer features
4. **Run notebook 3**: Train models

## 📊 Expected Results

- **Dataset**: ~119,000 hotel bookings
- **Cancellation Rate**: ~37% of bookings are canceled
- **Features**: 27+ engineered features
- **Models**: Logistic Regression and Random Forest
- **Performance**: Typically 75-85% accuracy

## 🔧 Requirements

```python
pandas
numpy
scikit-learn
joblib
```

## 💡 Tips

- **Run in order**: Each notebook depends on outputs from the previous one
- **Keep outputs**: Don't delete the `data/` and `artifacts/` folders
- **Experiment**: Try modifying features and model parameters
- **Document**: Add your own markdown cells with observations

## 📈 What You'll Learn

1. **Data Exploration**: How to analyze booking patterns
2. **Feature Engineering**: Creating meaningful features from raw data
3. **Data Preprocessing**: Handling missing values, encoding, scaling
4. **Model Training**: Building classification models
5. **Model Evaluation**: Comparing models with multiple metrics
6. **Feature Importance**: Understanding which features matter most

## 🎯 Project Goals

- **Primary**: Predict which bookings will be canceled
- **Secondary**: Understand factors that lead to cancellations
- **Business Value**: Help hotels optimize booking strategies and reduce cancellations

## 📝 Notes

- All notebooks use simple code for easy understanding
- Text-based outputs instead of complex visualizations
- Class balancing applied to handle imbalanced data
- Random state set to 42 for reproducibility

## 🤔 Common Issues

**Issue**: "File not found" error
**Solution**: Make sure `hotel_bookings.csv` is in the `../data/` folder

**Issue**: "Module not found" error
**Solution**: Install required packages: `pip install pandas numpy scikit-learn joblib`

**Issue**: "Artifact not found" error
**Solution**: Run the notebooks in order from 01 to 03

## 🔄 Re-running Notebooks

If you need to re-run:
1. Delete files in `data/` (except hotel_bookings.csv)
2. Delete files in `artifacts/`
3. Run notebooks 01, 02, 03 in order

Happy modeling! 🎉
