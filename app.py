import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    recommended_movie_list=[]
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:
        recommended_movie_list.append(movies.iloc[i[0]].title)
    return recommended_movie_list





movies_dict=pickle.load(open("movies_dict.pkl",'rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl",'rb'))

st.title("Movie Recommender system")

selected_movie_name=st.selectbox('Choose your movie',(movies['title'].values))

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
