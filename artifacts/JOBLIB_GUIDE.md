# 📦 Joblib Quick Guide

Simple guide to save and load machine learning models.

---

## 🎯 What is Joblib?

Joblib helps you **save** your trained models to files and **load** them later.

Think of it like **Save/Load** in a video game - but for your ML models! 🎮

---

## 📥 Installation

```bash
pip install joblib
```

---

## 💾 Saving a Model (3 Steps)

```python
import joblib

# Step 1: Train your model
model.fit(X_train, y_train)

# Step 2: Save it
joblib.dump(model, 'model.joblib')

# Step 3: Done! ✅
```

---

## 📂 Loading a Model (2 Steps)

```python
import joblib

# Step 1: Load the model
model = joblib.load('model.joblib')

# Step 2: Use it to predict
predictions = model.predict(X_test)
```

---

## 🔄 Complete Example

### Training & Saving

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

# Train
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save
joblib.dump(model, 'my_model.joblib')
print("Model saved! ✅")
```

### Loading & Predicting

```python
import joblib

# Load
model = joblib.load('my_model.joblib')

# Predict
predictions = model.predict(new_data)
print("Predictions done! ✅")
```

---

## 📁 Save Multiple Files

```python
import joblib

# Save model
joblib.dump(model, 'artifacts/model.joblib')

# Save scaler
joblib.dump(scaler, 'artifacts/scaler.joblib')

# Save feature names
joblib.dump(feature_names, 'artifacts/features.joblib')
```

---

## 📥 Load Multiple Files

```python
import joblib

# Load everything
model = joblib.load('artifacts/model.joblib')
scaler = joblib.load('artifacts/scaler.joblib')
features = joblib.load('artifacts/features.joblib')
```

---

## 🎁 Pro Tip: Save Everything Together

```python
import joblib

# Save multiple things in one file
everything = {
    'model': model,
    'scaler': scaler,
    'features': feature_names
}
joblib.dump(everything, 'artifacts/all.joblib')

# Load everything
everything = joblib.load('artifacts/all.joblib')
model = everything['model']
scaler = everything['scaler']
```

---

## 🚀 Use in Streamlit

```python
import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load('artifacts/model.joblib')

# Load once, use everywhere
model = load_model()
predictions = model.predict(data)
```

---

## ✅ Quick Cheat Sheet

| Task | Code |
|------|------|
| Save | `joblib.dump(model, 'model.joblib')` |
| Load | `model = joblib.load('model.joblib')` |
| Save with compression | `joblib.dump(model, 'model.joblib', compress=3)` |
| Check file exists | `os.path.exists('model.joblib')` |

---

## 🐛 Common Issues

**Problem:** "File not found"
```python
# Solution: Check path
import os
if os.path.exists('model.joblib'):
    model = joblib.load('model.joblib')
else:
    print("File not found!")
```

**Problem:** "Large file size"
```python
# Solution: Use compression
joblib.dump(model, 'model.joblib', compress=3)
```

---

## 📚 Summary

1. **Train** your model → `model.fit(X, y)`
2. **Save** your model → `joblib.dump(model, 'file.joblib')`
3. **Load** your model → `model = joblib.load('file.joblib')`
4. **Use** your model → `model.predict(new_data)`

**That's it!** 🎉

---

*For more details, visit: https://joblib.readthedocs.io*
