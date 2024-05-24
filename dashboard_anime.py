import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('processed_anime.csv')

# Convert columns to correct data types
df['episodes'] = pd.to_numeric(df['episodes'], errors='coerce')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['members'] = pd.to_numeric(df['members'], errors='coerce')

# Preprocess genre data to get the sum of each genre's occurrence
genre_counts = df['genre'].str.split(', ').explode().value_counts().reset_index() 
genre_counts.columns = ['genre', 'count']

# Streamlit app layout
st.title("Anime Streaming")
st.subheader(" ", divider='grey')
st.write("")
st.write("")

# Sidebar for filters
st.sidebar.header("Filters")
genre_filter = st.sidebar.multiselect("Select Genre", genre_counts['genre'])
type_filter = st.sidebar.multiselect("Select Type", df['type'].unique())
episode_filter = st.sidebar.slider("Number of Episodes", min_value=1, max_value=100, value=(1, 100))
rating_filter = st.sidebar.slider("Rating", min_value=0.0, max_value=10.0, value=(0.0, 10.0))
member_filter = st.sidebar.slider("Number of Members", min_value=0, max_value=20000, value=(0, 20000))

# Filter the dataframe based on user selection
filtered_df = df[
    (df['genre'].str.split(', ').explode().isin(genre_filter).groupby(level=0).any() if genre_filter else True) &
    (df['type'].isin(type_filter) if type_filter else True) &
    (df['episodes'] >= episode_filter[0]) & (df['episodes'] <= episode_filter[1]) &
    (df['rating'] >= rating_filter[0]) & (df['rating'] <= rating_filter[1]) &
    (df['members'] >= member_filter[0]) & (df['members'] <= member_filter[1])
]

# Group by anime name and aggregate data
grouped_df = filtered_df.groupby('name').agg({
    'episodes': 'sum',
    'rating': 'mean',
    'members': 'sum'
}).reset_index()
    
# Common layout settings for font sizes
layout_settings = {
    'xaxis_title_font_size': 18,
    'yaxis_title_font_size': 18,
    'xaxis_tickfont_size': 14,
    'yaxis_tickfont_size': 14,
    'legend_font_size': 16,
    'title_font_size': 24
}

# Top 10 Anime by Rating
top_10_anime = grouped_df.nlargest(10, 'rating')[['name', 'rating']]
fig1 = px.bar(top_10_anime, x='rating', y='name', orientation='h', title='Top 10 Anime by Rating', color_discrete_sequence=['#9932cc'])
fig1.update_layout(xaxis_title='Rating', yaxis_title='Anime name', title_x=0.35, **layout_settings)
st.plotly_chart(fig1)

# Genre Distribution
genre_df = filtered_df.copy()
genre_df = genre_df.assign(genre=genre_df['genre'].str.split(', ')).explode('genre')
fig2 = px.violin(genre_df, x='genre', y='rating', box=True, title='Genre Distribution', color_discrete_sequence=['#644dd3'])
fig2.update_layout(xaxis_title='Genre', yaxis_title='Rating', xaxis=dict(tickangle=-45), title_x=0.35, **layout_settings)
st.plotly_chart(fig2)

# Rating vs. Members Scatter Plot
fig3 = px.scatter(grouped_df, x='rating', y='members', title='Relation between Rating and Members', color_discrete_sequence=['#9932cc'])
fig3.update_traces(marker=dict(opacity=0.6))
fig3.update_layout(xaxis_title='Rating', yaxis_title='Members', title_x=0.2, **layout_settings)
st.plotly_chart(fig3)

# Bubble Chart: Rating vs. Episodes with Members as Size
fig4 = px.scatter(grouped_df, x='rating', y='episodes', size='members', title='Relation among Rating, Episodes and Members', labels={'rating': 'Rating', 'members': 'Members', 'episodes': 'Number of Episodes'},
                  color_discrete_sequence=['#3265cc'])
fig4.update_layout(xaxis_title='Rating', yaxis_title='Episodes', title_x=0.15, **layout_settings)
st.plotly_chart(fig4)

# Type Distribution (Strip Plot)
fig5 = px.strip(filtered_df, x='type', y='rating', title='Distribution of Anime Types', color='type',
                color_discrete_sequence=['#9932cc'])
fig5.update_traces(marker=dict(opacity=0.6))
fig5.update_layout(xaxis_title='Type', yaxis_title='Rating', title_x=0.3, **layout_settings)
st.plotly_chart(fig5)

# Episodes vs. Rating
episodes_rating = filtered_df.groupby('episodes')['rating'].mean().reset_index()
fig6 = px.line(episodes_rating, x='episodes', y='rating', markers=True, title='Episode Count Impact on Anime Average Ratings', color_discrete_sequence=['#644dd3'])
fig6.update_layout(xaxis_title='Number of Episodes', yaxis_title='Average Rating', title_x=0.16, **layout_settings)
st.plotly_chart(fig6)

# Add a button that accesses a website
st.link_button("Visit MyAnimeList Website", "https://myanimelist.net/")
