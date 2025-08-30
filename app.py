import pickle
import streamlit as st
import pandas as pd

# =========================
# Load Data
# =========================
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# =========================
# Recommend Function
# =========================
def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return []

    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommended_movies

# =========================
# Streamlit UI
# =========================
st.set_page_config(page_title=" Movie Recommender", page_icon="🎬", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #fff;
            font-family: 'Poppins', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 45px;
            font-weight: 700;
            color: #E50914;
            margin-bottom: 20px;
        }
        .recommendation {
            background-color: lightgray;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: center;
            font-size: 18px;
            font-weight: 600;
            color: black;
            transition: 0.3s;
        }
        .recommendation:hover {
            background-color: gray;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🍿 Movie Recommender System</div>", unsafe_allow_html=True)

# Movie selection
selected_movie_name = st.selectbox("🎥 Select a Movie:", movies['title'].values)

# Recommend Button
if st.button("🔍 Recommend"):
    recommendations = recommend(selected_movie_name)
    if recommendations:
        st.subheader("✅ Recommended Movies:")
        for movie in recommendations:
            st.markdown(f"<div class='recommendation'>{movie}</div>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found for this movie.")




