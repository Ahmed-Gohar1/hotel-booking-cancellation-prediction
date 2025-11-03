import os
import streamlit as st
import pandas as pd
import joblib


st.title("🏨 Hotel Booking Cancellation Predictor")
ROOT = os.path.dirname(__file__)
MODEL_PATH = os.path.join(ROOT, "notebooks", "artifacts", "best_model.joblib")


@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    return model


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Preprocess hotel booking data for prediction"""
    X = df.copy()
    
    # Create derived features
    X['total_guests'] = X['adults'] + X['children'].fillna(0) + X['babies'].fillna(0)
    X['total_nights'] = X['stays_in_weekend_nights'] + X['stays_in_week_nights']
    
    # Convert numeric columns
    numeric_cols = ['lead_time', 'stays_in_weekend_nights', 'stays_in_week_nights',
                    'adults', 'children', 'babies', 'is_repeated_guest',
                    'previous_cancellations', 'previous_bookings_not_canceled',
                    'booking_changes', 'days_in_waiting_list', 'adr',
                    'required_car_parking_spaces', 'total_of_special_requests',
                    'total_guests', 'total_nights']
    
    for col in numeric_cols:
        if col in X.columns:
            X[col] = pd.to_numeric(X[col], errors='coerce')
    
    # One-hot encode categorical variables
    categorical_cols = ['hotel', 'arrival_date_month', 'meal', 'country',
                        'market_segment', 'distribution_channel', 'reserved_room_type',
                        'assigned_room_type', 'deposit_type', 'customer_type']
    
    X_enc = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
    
    # Fill missing values with 0
    X_enc = X_enc.fillna(0)
    
    # Select only numeric columns for prediction
    X_numeric = X_enc.select_dtypes(include=['number'])
    
    return X_numeric


st.sidebar.markdown("### 📤 Upload CSV File")
st.sidebar.markdown("Upload a CSV with the same columns as hotel_bookings.csv")
uploaded = st.sidebar.file_uploader("CSV file", type=["csv"])

if not os.path.exists(MODEL_PATH):
    st.warning(f"❌ Model not found at {MODEL_PATH}")
    st.info("💡 Run the training notebook (03_model_training.ipynb) to create it.")
else:
    model = load_model()
    st.success("✅ Model loaded successfully!")
    
    if uploaded is not None:
        try:
            # Read uploaded data
            df = pd.read_csv(uploaded)
            st.write(f"**📊 Uploaded Data:** {len(df)} bookings")
            
            # Show preview
            with st.expander("👀 Preview uploaded data"):
                st.dataframe(df.head(10))
            
            # Preprocess
            with st.spinner("Processing data..."):
                X = preprocess(df)
            
            # Get model's expected features
            try:
                model_features = model.feature_names_in_
                X_aligned = X.reindex(columns=model_features, fill_value=0)
            except AttributeError:
                # If model doesn't have feature_names_in_, use all columns
                X_aligned = X
            
            # Make predictions
            with st.spinner("Making predictions..."):
                preds = model.predict(X_aligned)
                probs = model.predict_proba(X_aligned)[:, 1]
            
            # Add predictions to output
            out = df.copy()
            out["cancellation_prediction"] = preds
            out["cancellation_probability"] = probs
            out["risk_level"] = pd.cut(probs, 
                                       bins=[0, 0.3, 0.7, 1.0], 
                                       labels=['Low', 'Medium', 'High'])
            
            # Display summary metrics
            st.markdown("---")
            st.subheader("📊 Prediction Results")
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Predicted Cancellations", f"{preds.sum()}")
            with col2:
                st.metric("Cancellation Rate", f"{preds.mean()*100:.1f}%")
            with col3:
                st.metric("Avg Probability", f"{probs.mean()*100:.1f}%")
            
            # Show risk distribution
            st.markdown("### 🎯 Risk Distribution")
            risk_counts = out['risk_level'].value_counts()
            st.bar_chart(risk_counts)
            
            # Display results table
            st.markdown("### 📋 Detailed Predictions")
            display_cols = ['cancellation_prediction', 'cancellation_probability', 'risk_level']
            
            # Add useful columns if they exist
            for col in ['hotel', 'lead_time', 'adr', 'arrival_date_month', 'market_segment']:
                if col in out.columns and col not in display_cols:
                    display_cols.insert(0, col)
            
            st.dataframe(out[display_cols].head(20), use_container_width=True)
            
            # Download button
            st.markdown("---")
            st.download_button(
                label="📥 Download Full Predictions (CSV)",
                data=out.to_csv(index=False),
                file_name="hotel_cancellation_predictions.csv",
                mime="text/csv"
            )
            
        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            st.info("Make sure your CSV has the same columns as hotel_bookings.csv")
            
    else:
        st.info("👆 Upload a CSV file to get predictions")
        st.markdown("""
        ### 📝 Required Columns:
        Your CSV should include:
        - `hotel`, `lead_time`, `arrival_date_month`, `arrival_date_year`
        - `stays_in_weekend_nights`, `stays_in_week_nights`
        - `adults`, `children`, `babies`
        - `meal`, `market_segment`, `distribution_channel`
        - `is_repeated_guest`, `previous_cancellations`, `booking_changes`
        - `deposit_type`, `customer_type`
        - `adr`, `required_car_parking_spaces`, `total_of_special_requests`
        
        ### 🧪 Test Files Available:
        Check the `test_data` folder for 5 ready-to-use test files:
        - `test_high_risk.csv` - High cancellation risk bookings
        - `test_low_risk.csv` - Low cancellation risk bookings
        - `test_business_travelers.csv` - Business customer bookings
        - `test_family_vacation.csv` - Family vacation bookings
        - `test_mixed.csv` - Mixed risk scenarios
        """)
