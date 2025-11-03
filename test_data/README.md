# Hotel Booking Cancellation Test Data

This folder contains 5 test CSV files to test the cancellation prediction model in the Streamlit app.

## 📋 Test Files Overview

### 1. `test_high_risk.csv` (8 bookings) ⚠️ HIGH RISK
**Characteristics:**
- Very long lead times (320-450 days)
- Previous cancellation history (1-4 cancellations)
- Online travel agency bookings
- Low special requests (0-1)
- No deposit required

**Expected Result:** High cancellation probability (70-90%)

---

### 2. `test_low_risk.csv` (8 bookings) ✅ LOW RISK
**Characteristics:**
- Short lead times (10-30 days)
- Repeated guests with good history
- Direct or corporate bookings
- Multiple special requests (2-5)
- Good previous booking record (8-15 completed bookings)

**Expected Result:** Low cancellation probability (10-30%)

---

### 3. `test_mixed.csv` (10 bookings) 🔄 MIXED RISK
**Characteristics:**
- Varied lead times (10-380 days)
- Mix of new and repeated guests
- Different booking channels
- Various cancellation histories
- Different customer types

**Expected Result:** Mixed probabilities (20-70%)

---

### 4. `test_business_travelers.csv` (10 bookings) 💼 BUSINESS
**Characteristics:**
- Very short lead times (5-15 days)
- Corporate bookings with company ID
- Repeated guests (contract customers)
- Same agent (Agent 40, Company 223)
- Single adults, short stays (1-4 nights)

**Expected Result:** Very low cancellation probability (5-20%)

---

### 5. `test_family_vacation.csv` (10 bookings) 👨‍👩‍👧‍👦 VACATION
**Characteristics:**
- Moderate lead times (85-150 days)
- Resort hotel bookings
- Multiple guests (2-3 adults, children)
- Long stays (9-14 nights)
- Many special requests (4-8)
- Full board or half board meals

**Expected Result:** Low to moderate cancellation probability (20-40%)

---

## 🚀 How to Use

1. **Start the Streamlit app:**
   ```powershell
   cd d:\projects\5
   streamlit run app.py
   ```

2. **Go to the "Prediction" tab**

3. **Upload any test file** from the sidebar

4. **View results:**
   - Cancellation predictions
   - Probability scores
   - Risk distribution chart
   - Download predictions as CSV

---

## 📊 Expected Results Summary

| Test File | Expected Cancellations | Avg Probability | Risk Level |
|-----------|----------------------|-----------------|------------|
| High Risk | 6-8 / 8 | 70-85% | High |
| Low Risk | 1-3 / 8 | 15-25% | Low |
| Mixed | 4-6 / 10 | 35-55% | Mixed |
| Business | 0-2 / 10 | 10-18% | Low |
| Family Vacation | 2-4 / 10 | 25-35% | Low-Med |

---

## 🎯 Test Scenarios Explained

### High Risk Factors:
- ❌ Long lead time (>300 days)
- ❌ Previous cancellations
- ❌ Online TA bookings
- ❌ No deposit
- ❌ Few special requests

### Low Risk Factors:
- ✅ Short lead time (<30 days)
- ✅ Repeated guest
- ✅ Direct/Corporate booking
- ✅ Many special requests
- ✅ Clean booking history
- ✅ Deposit required

### Key Insights:
- **Business travelers** = Most reliable (corporate contracts)
- **Family vacations** = Moderate risk (planned ahead)
- **Last-minute bookings** = Generally lower risk
- **Long lead time + OTA** = Highest risk combination
