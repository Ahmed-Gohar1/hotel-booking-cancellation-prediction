# 🚀 Running the Streamlit App

This guide shows you how to run the Hotel Booking Cancellation Predictor Streamlit app.

---

## 📋 Prerequisites

Make sure you have:
- ✅ Python installed (3.8 or higher)
- ✅ Streamlit installed (`pip install streamlit`)
- ✅ Required packages installed (`pip install -r requirements.txt`)
- ✅ Trained model in `notebooks/artifacts/best_model.joblib`

---

## 🎯 Method 1: Run from Project Root (Recommended)

```bash
# Navigate to project directory
cd /path/to/hotel-booking-project

# Run the app
streamlit run app_simple.py
```

**Windows:**
```powershell
cd C:\path\to\hotel-booking-project
streamlit run app_simple.py
```

---

## 🎯 Method 2: Run with Full Path

**Linux/Mac:**
```bash
streamlit run /path/to/hotel-booking-project/app_simple.py
```

**Windows:**
```powershell
streamlit run "C:\path\to\hotel-booking-project\app_simple.py"
```

---

## 🎯 Method 3: Run from Any Directory

**Linux/Mac:**
```bash
cd /path/to/hotel-booking-project
streamlit run app_simple.py
```

**Windows:**
```powershell
cd C:\path\to\hotel-booking-project
streamlit run app_simple.py
```

---

## 🎯 Method 4: Run with Custom Port

```bash
# Run on a different port (e.g., 8502)
streamlit run app_simple.py --server.port 8502
```

---

## 🎯 Method 5: Run in Development Mode (Auto-reload)

```bash
# Runs with auto-reload on file changes
streamlit run app_simple.py --server.runOnSave true
```

---

## 🌐 Accessing the App

Once the app starts, you'll see:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.20:8501
```

**Open in browser:**
- **Local access:** http://localhost:8501
- **Network access:** http://192.168.1.20:8501 (from other devices on same network)

---

## 🛑 Stopping the App

Press `Ctrl + C` in the terminal where Streamlit is running.

**Or use command line to kill the process:**

**Linux/Mac:**
```bash
# Find and kill Streamlit process
pkill -f streamlit
```

**Windows:**
```powershell
# Stop all Streamlit processes
taskkill /F /IM streamlit.exe
```

---

## 🧪 Testing the App

After the app starts:

1. **Upload a test CSV file** from the `test_data` folder:
   - `test_high_risk.csv`
   - `test_low_risk.csv`
   - `test_business_travelers.csv`
   - `test_family_vacation.csv`
   - `test_mixed.csv`

2. **View predictions** with probability scores

3. **Download results** as CSV

---

## ⚙️ Configuration Options

### Change Default Browser

```bash
streamlit run app_simple.py --server.headless false
```

### Run Without Opening Browser

```bash
streamlit run app_simple.py --server.headless true
```

### Enable CORS (for external access)

```bash
streamlit run app_simple.py --server.enableCORS false
```

---

## 🐛 Troubleshooting

### Issue: "Model not found"
**Solution:** Run the training notebook first:
```bash
# Using Jupyter Notebook
jupyter notebook notebooks/03_model_training.ipynb

# Or using JupyterLab
jupyter lab notebooks/03_model_training.ipynb
```

### Issue: "Port already in use"
**Solution:** Use a different port:
```bash
streamlit run app_simple.py --server.port 8502
```

### Issue: "Module not found"
**Solution:** Install requirements:
```bash
pip install -r requirements.txt
```

### Issue: App doesn't open automatically
**Solution:** Manually open http://localhost:8501 in your browser

---

## 📦 Quick Start (All-in-One)

**Linux/Mac:**
```bash
# Complete workflow
cd /path/to/hotel-booking-project
pip install -r requirements.txt
streamlit run app_simple.py
```

**Windows:**
```powershell
# Complete workflow
cd C:\path\to\hotel-booking-project
pip install -r requirements.txt
streamlit run app_simple.py
```

---

## 🔗 Useful Streamlit Commands

```bash
# Check Streamlit version
streamlit --version

# View Streamlit help
streamlit --help

# Clear Streamlit cache
streamlit cache clear

# Run with specific config
streamlit run app_simple.py --server.fileWatcherType none
```

---

## 📚 Additional Resources

- **Streamlit Documentation:** https://docs.streamlit.io
- **Project README:** See `README.md` for project details
- **Test Data Info:** See `test_data/README.md` for test file descriptions

---

## ✅ Success!

If you see the app running at http://localhost:8501, you're all set! 🎉

Upload a CSV file and start predicting hotel booking cancellations! 🏨
