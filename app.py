
 
import pickle
import streamlit as st
import pandas as pd

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]  
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)  
    return recommended_movies
        
# Load Data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit 
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a Movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for movie in recommendations:
        st.write(movie)



