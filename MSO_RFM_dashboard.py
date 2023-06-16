import streamlit as st
import plotly.express as px
import pandas as pd
df = pd.read_csv('/Users/samharvey/Desktop/rmf_data_labels.csv')
subscribers_df = df[df['subscriber'] == 'Y'].copy()
non_subscribers_df = df[df['subscriber'] == 'N'].copy()

# Create the three scatter plots
fig_all = px.scatter_3d(df, x='recency', y='frequency', z='revenue', color='Segment')
fig_subscribers = px.scatter_3d(subscribers_df, x='recency', y='frequency', z='revenue', color='Segment')
fig_non_subscribers = px.scatter_3d(non_subscribers_df, x='recency', y='frequency', z='revenue', color='Segment')

# Define the layout of the dashboard
st.set_page_config(layout="wide")
st.title("MSO RFM Segmentation Dashboard")
option = st.selectbox("Select Plot", ("All Customers", "Subscribers", "Non-Subscribers"))

if option == "All Customers":
    st.plotly_chart(fig_all, use_container_width=True)
elif option == "Subscribers":
    st.plotly_chart(fig_subscribers, use_container_width=True)
elif option == "Non-Subscribers":
    st.plotly_chart(fig_non_subscribers, use_container_width=True)
