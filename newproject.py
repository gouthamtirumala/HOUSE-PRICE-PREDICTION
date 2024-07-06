import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

st.image(r"C:\inno image.jpeg")
st.title("HOUSE PRICE PREDICTION")
model = pickle.load(open(r"C:\Users\HP\Downloads\lr.pkl","rb"))

SquareFeet = st.number_input("Enter Area of house in square feet",min_value = 600, max_value = 5000, step = 50)
Bedrooms = st.number_input("Enter the number of bedrooms",min_value = 0, max_value = 5, step = 1)	
Bathrooms = st.number_input("Enter the number of bathrooms",min_value = 0, max_value = 5, step = 1)	
Neighborhood = st.radio("Select type of neighbourhood",['Rural','Urban','Suburb'])
neighbor = 1 if Neighborhood=="Rural" else 2 if Neighborhood=="Urban" else 3

YearBuilt = st.number_input("Enter year of Construction of property",min_value = 1900, max_value = 2030, step = 1)

price = model.predict([[SquareFeet,Bedrooms,Bathrooms,neighbor,YearBuilt]])

if st.button("PREDICT PRICE"):
    st.write("The price for the flat with given details is Rs.",price)
