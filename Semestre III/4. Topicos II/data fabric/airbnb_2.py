# Import necessary libraries
import streamlit as st
from pymongo import MongoClient
import matplotlib.pyplot as plt
import pandas as pd

client = MongoClient("mongodb+srv://robramirez:redacted@streamlit.trtuhs7.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_airbnb
collection = db.listingsAndReviews

data = pd.DataFrame(list(collection.find()))

st.title("Airbnb Data from MongoDB")
st.text('Roberto Ramirez ')

st.write("## Data from MongoDB Atlas:")
st.write(data.head())

st.write("## Number of Listings per Property Type")
property_type_counts = data['property_type'].value_counts().sort_values(ascending=False)

st.bar_chart(property_type_counts)

