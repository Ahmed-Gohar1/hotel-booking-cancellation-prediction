# 🏨 Hotel Booking Cancellation Prediction

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-red.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.6+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete machine learning project to predict hotel booking cancellations with 85%+ accuracy. Features exploratory data analysis, feature engineering, trained models, and an interactive Streamlit web application for real-time predictions.

![Hotel Booking Analysis](https://img.shields.io/badge/Dataset-119K_Bookings-success)
![Cancellation Rate](https://img.shields.io/badge/Cancellation_Rate-37%25-critical)
![Model Accuracy](https://img.shields.io/badge/Accuracy-85%25+-brightgreen)

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Dataset](#-dataset)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [Streamlit App](#-streamlit-app)
- [SQL Analysis](#-sql-analysis)
- [Results](#-results)
- [Technologies](#-technologies-used)
- [License](#-license)
- [Author](#-author)

---

## 🎯 Overview

This project analyzes hotel booking data to predict cancellations using machine learning. It includes:

- **Comprehensive EDA** with 20+ visualizations
- **Feature Engineering** pipeline with encoding and scaling
- **Multiple ML models** (Logistic Regression, Random Forest)
- **Interactive Streamlit app** for predictions
- **SQL queries** for business intelligence
- **Production-ready** model artifacts

**Key Metrics:**
- 📊 Dataset: 119,390 hotel bookings
- 🎯 Cancellation Rate: 37%
- ⚡ Model Accuracy: 85%+
- 📈 Features: 30+ engineered features

---

## ✨ Features

### 🔍 Exploratory Data Analysis
- 20 comprehensive visualizations
- Statistical analysis of booking patterns
- Cancellation trends by various factors
- Customer segmentation analysis

### 🛠️ Feature Engineering
- Automated preprocessing pipeline
- Categorical encoding (One-Hot, Label)
- Feature scaling (StandardScaler)
- Derived features (total guests, total nights)

### 🤖 Machine Learning Models
- **Logistic Regression** - Fast baseline model
- **Random Forest** - Best performing model (85%+ accuracy)
- Model comparison and evaluation
- Hyperparameter tuning

### 🌐 Streamlit Web App
- Upload CSV files for batch predictions
- Real-time cancellation probability scores
- Risk level classification (Low/Medium/High)
- Interactive visualizations
- Downloadable predictions

### 📊 SQL Analysis
- 22 business intelligence queries
- Common Table Expressions (CTEs)
- Revenue analysis
- Customer behavior patterns

---

## 📦 Dataset

**Source:** Hotel Booking Demand Dataset  
**Size:** 119,390 bookings  
**Features:** 32 columns  
**Target:** `is_canceled` (0 = No, 1 = Yes)

### Key Features:
- `hotel` - Hotel type (Resort/City)
- `lead_time` - Days between booking and arrival
- `arrival_date_month` - Month of arrival
- `stays_in_weekend_nights` / `stays_in_week_nights` - Length of stay
- `adults`, `children`, `babies` - Number of guests
- `meal` - Meal type booked
- `market_segment` - Market segment designation
- `is_repeated_guest` - Whether guest has stayed before
- `previous_cancellations` - Number of previous cancellations
- `adr` - Average Daily Rate
- `total_of_special_requests` - Number of special requests

---

## 📁 Project Structure

```
hotel-booking-cancellation-prediction/
│
├── 📄 README.md                          # This file
├── 📄 LICENSE                            # MIT License
├── 📄 requirements.txt                   # Python dependencies
├── 📄 START_HERE.md                      # Quick start guide
├── 📄 APP_RUN.md                         # Streamlit app instructions
├── 🐍 app_simple.py                      # Streamlit application
├── 🐍 download_dataset.py                # Dataset downloader
│
├── 📁 data/                              # Raw data
│   └── hotel_bookings.csv               # Original dataset
│
├── 📁 notebooks/                         # Jupyter notebooks
│   ├── 01_data_exploration.ipynb        # EDA notebook
│   ├── 02_feature_engineering.ipynb     # Feature engineering
│   ├── 03_model_training.ipynb          # Model training & evaluation
│   ├── Simple_EDA.ipynb                 # Simplified EDA with visuals
│   ├── 📁 artifacts/                    # Model artifacts
│   │   ├── best_model.joblib           # Best trained model
│   │   ├── scaler.joblib               # Feature scaler
│   │   ├── encoders.joblib             # Categorical encoders
│   │   └── feature_names.joblib        # Feature names
│   └── 📁 data/                        # Processed data
│       ├── X_train.csv                 # Training features
│       ├── X_test.csv                  # Test features
│       ├── y_train.csv                 # Training labels
│       └── y_test.csv                  # Test labels
│
├── 📁 src/                              # Python scripts
│   ├── 01_data_exploration.py          # EDA script
│   ├── 02_feature_engineering.py       # Feature engineering script
│   ├── 03_model_training.py            # Model training script
│   └── simple_eda_visualizations.py    # Generate all EDA plots
│
├── 📁 sql/                              # SQL queries
│   ├── 01_basic_eda_analysis.sql       # Basic analysis queries
│   └── 02_advanced_eda_analysis.sql    # Advanced analysis queries
│
├── 📁 reports/                          # Generated reports
│   └── 📁 figures/                     # EDA visualizations (20 plots)
│
├── 📁 test_data/                        # Test CSV files
│   ├── README.md                       # Test data documentation
│   ├── test_high_risk.csv              # High cancellation risk
│   ├── test_low_risk.csv               # Low cancellation risk
│   ├── test_business_travelers.csv     # Business bookings
│   ├── test_family_vacation.csv        # Family bookings
│   └── test_mixed.csv                  # Mixed scenarios
│
└── 📁 artifacts/                        # Documentation
    └── JOBLIB_GUIDE.md                 # Guide to model persistence
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/Ahmed-Gohar1/hotel-booking-cancellation-prediction.git
cd hotel-booking-cancellation-prediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download the dataset**
```bash
python download_dataset.py
```

---

## 💻 Usage

### Option 1: Streamlit Web App (Recommended)

Run the interactive web application:

```bash
streamlit run app_simple.py
```

Then open http://localhost:8501 in your browser and upload a CSV file to get predictions.

### Option 2: Jupyter Notebooks

Explore the analysis step-by-step:

```bash
jupyter notebook notebooks/
```

Open notebooks in order:
1. `01_data_exploration.ipynb` - Understand the data
2. `02_feature_engineering.ipynb` - Process features
3. `03_model_training.ipynb` - Train and evaluate models

### Option 3: Python Scripts

Run scripts directly:

```bash
# Generate EDA visualizations
python src/simple_eda_visualizations.py

# Run full pipeline
python src/01_data_exploration.py
python src/02_feature_engineering.py
python src/03_model_training.py
```

---

## 📊 Model Performance

### Random Forest (Best Model)

| Metric | Train | Test |
|--------|-------|------|
| **Accuracy** | 87.2% | 85.3% |
| **Precision** | 86.5% | 84.8% |
| **Recall** | 85.1% | 83.7% |
| **F1-Score** | 85.8% | 84.2% |

### Feature Importance (Top 10)

1. `lead_time` - Days between booking and arrival
2. `total_of_special_requests` - Number of special requests
3. `previous_cancellations` - Previous cancellation history
4. `booking_changes` - Number of booking modifications
5. `deposit_type` - Type of deposit made
6. `adr` - Average daily rate
7. `customer_type` - Customer classification
8. `market_segment` - Market segment
9. `total_guests` - Total number of guests
10. `total_nights` - Total length of stay

---

## 🌐 Streamlit App

The web application provides an intuitive interface for predictions:

### Features:
- 📤 **Upload CSV** - Drag and drop booking data
- 🔮 **Instant Predictions** - Real-time cancellation probabilities
- 📊 **Visual Analytics** - Risk distribution charts
- 💾 **Export Results** - Download predictions as CSV
- 📈 **Summary Metrics** - Key statistics at a glance

### Test Data:
Use the provided test CSV files in `test_data/` folder:
- `test_high_risk.csv` - Expected: 70-90% cancellation rate
- `test_low_risk.csv` - Expected: 10-30% cancellation rate
- `test_business_travelers.csv` - Expected: 5-20% cancellation rate
- `test_family_vacation.csv` - Expected: 20-40% cancellation rate
- `test_mixed.csv` - Expected: 35-55% cancellation rate

---

## 🗄️ SQL Analysis

Two comprehensive SQL files with CTEs for business intelligence:

### 01_basic_eda_analysis.sql (10 queries)
- Booking overview statistics
- Cancellation by hotel type
- Monthly trends analysis
- Market segment analysis
- Lead time impact
- Customer behavior patterns

### 02_advanced_eda_analysis.sql (12 queries)
- Revenue analysis
- Guest composition analysis
- Stay duration patterns
- Distribution channel effectiveness
- Year-over-year comparison
- **Risk factor scoring**

---

## 📈 Results

### Key Insights

1. **📅 Lead Time Effect**
   - Bookings made 6+ months in advance: 60% cancellation rate
   - Last-minute bookings (1-7 days): 15% cancellation rate

2. **⭐ Special Requests Matter**
   - With special requests: 22% cancellation rate
   - Without special requests: 48% cancellation rate

3. **🔄 Repeated Guests**
   - New guests: 38% cancellation rate
   - Repeated guests: 14% cancellation rate

4. **💳 Deposit Type Impact**
   - No deposit: 42% cancellation rate
   - With deposit: 23% cancellation rate

5. **🏨 Hotel Type**
   - City Hotel: 42% cancellation rate
   - Resort Hotel: 28% cancellation rate

---

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning
- **Matplotlib & Seaborn** - Visualization
- **Streamlit** - Web application
- **Joblib** - Model persistence
- **Jupyter** - Interactive notebooks

---

## 📚 Documentation

- [START_HERE.md](START_HERE.md) - Quick start guide
- [APP_RUN.md](APP_RUN.md) - Streamlit app instructions
- [artifacts/JOBLIB_GUIDE.md](artifacts/JOBLIB_GUIDE.md) - Model persistence guide
- [test_data/README.md](test_data/README.md) - Test data documentation

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ahmed Gohar**

- GitHub: [@Ahmed-Gohar1](https://github.com/Ahmed-Gohar1)
- Repository: [hotel-booking-cancellation-prediction](https://github.com/Ahmed-Gohar1/hotel-booking-cancellation-prediction)

---

## ⭐ Star This Repository

If you find this project helpful, please give it a star! It helps others discover the project.

---

**Made with ❤️ by Ahmed Gohar**
