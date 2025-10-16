import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers. Data: metadata.csv from Kaggle (sample used here).")

# Load sample data
df = pd.read_csv('sample_metadata.csv')

# Interactive widgets
year_range = st.slider("Select Year Range", int(df['year'].min()), int(df['year'].max()), (2020, 2021))
selected_source = st.selectbox("Select Source", df['source_x'].unique())

# Filter data
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1]) & (df['source_x'] == selected_source)]

st.write(f"Filtered Papers: {len(filtered_df)}")
st.dataframe(filtered_df.head())  # Show sample

# Display pre-saved viz
st.header("Publications by Year")
image1 = Image.open('pubs_by_year.png')
st.image(image1)

st.header("Top Journals")
image2 = Image.open('top_journals.png')
st.image(image2)

st.header("Word Cloud")
image3 = Image.open('wordcloud_titles.png')
st.image(image3)

st.header("Sources Distribution")
image4 = Image.open('sources_pie.png')
st.image(image4)

# Simple dynamic viz
st.header("Papers in Selected Range")
year_counts_filtered = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
year_counts_filtered.plot(kind='bar', ax=ax)
st.pyplot(fig)

# Comments: Add your insights here
st.write("Insights: Spike in 2020 publications reflects pandemic response.")
