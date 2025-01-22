import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Streamlit web app
st.title("House Price Prediction App")

# Input form
st.header("Enter House Details:")
square_feet = st.number_input("Square Feet", min_value=100, max_value=10000, value=1000, step=50)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2, step=1)
neighborhood = st.selectbox("Neighborhood", options=["Rural", "Suburb", "Urban"])
year_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2000, step=1)

# Predict button
if st.button("Predict Price"):
    # Prepare input for the model
    input_data = pd.DataFrame({
        "SquareFeet": [square_feet],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Neighborhood": [neighborhood],
        "YearBuilt": [year_built]
    })
    
    # Predict price
    predicted_price = model.predict(input_data)[0]
    
    # Display result
    st.success(f"The predicted house price is ${predicted_price:,.2f}")

# Footer
st.write("This is a demo application for house price prediction.")
