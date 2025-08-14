import pandas as pd
import  streamlit as st
import pickle
import numpy as np

similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies = []
    for j in movies_list:
        recommended_movies.append(movies.iloc[j[0]].title)
    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


# to display title
st.title('Movie Recommender System')
# to display view option
selected_movie = st.selectbox('How would you like to be contacted ?',
                      movies['title'].values)

# recommend button
if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)