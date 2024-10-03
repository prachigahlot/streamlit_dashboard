# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
@st.cache_data   # Caches the dataset for faster loading
def load_data():
    github_data = pd.read_csv('data/github_dataset.csv')
    repo_data = pd.read_csv('data/repository_data.csv')
    return github_data, repo_data

# Load data
github_data, repo_data = load_data()

# Streamlit App Title and Description
st.title('GitHub Repositories Dashboard')
st.write('An interactive dashboard showcasing GitHub repository statistics.')

# Sidebar filters
st.sidebar.header('Filter by:')
languages = github_data['language'].unique().tolist()
selected_language = st.sidebar.multiselect('Select Programming Languages:', languages, default=languages)

# Filter data based on sidebar input
filtered_data = github_data[github_data['language'].isin(selected_language)]

# Show Dataframe
st.header('GitHub Repositories Overview')
st.write('Filtered GitHub Repositories based on the selected programming languages.')
st.dataframe(filtered_data)

# Visualization 1: Stars Count by Language
st.header('Stars Count by Programming Language')
st.write('Bar plot of total stars count for each programming language.')

# Group the data by language and sum the stars
stars_by_language = filtered_data.groupby('language')['stars_count'].sum().reset_index()

# Plot the data
fig1, ax1 = plt.subplots()

sns.barplot(data=stars_by_language, x='language', y='stars_count', ax=ax1)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig1)

# Visualization 2: Issues Count by Language
st.header('Issues Count by Programming Language')
st.write('Scatter plot of issues count for each repository.')

# Scatter plot of issues count by language
fig2, ax2 = plt.subplots()

sns.scatterplot(data=filtered_data, x='language', y='issues_count', size='stars_count', hue='language', ax=ax2, sizes=(20, 200))
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig2)

# Extra feature from `repositor_data`
st.header('Repository Creation Year and Stars')
st.write('Visualizing stars count with the repository creation year (from another dataset).')

# Convert the 'created_at' column to datetime
repo_data['created_at'] = pd.to_datetime(repo_data['created_at'])
repo_data['year'] = repo_data['created_at'].dt.year

# Line plot of stars over the years
stars_by_year = repo_data.groupby('year')['stars_count'].sum().reset_index()

fig3, ax3 = plt.subplots()
sns.lineplot(data=stars_by_year, x='year', y='stars_count', ax=ax3)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig3)

