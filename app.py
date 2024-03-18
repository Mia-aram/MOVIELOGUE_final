import pickle
import streamlit as st
import pdb
from tmdbv3api import Movie, TMDb


find_list = pickle.load(open('find_list.pickle', 'rb'))
total = pickle.load(open('total.pickle', 'rb'))
credits = pickle.load(open('credits.pickle', 'rb'))  
overView = pickle.load(open('overView.pickle', 'rb'))

# PDB
#l(list): 현재 위치 주변의 코드를 보여줍니다.
# n(next): 다음 줄로 이동합니다. 함수 호출을 건너뛸 수 있습니다.
# s(step): 다음 줄로 이동합니다. 함수 호출 내부로 들어갈 수 있습니다.
# p(print): 표현식을 출력합니다.
# q(quit): 디버거를 종료합니다.
def BreakPoint():
    pdb.set_trace()

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '06ebe2f988bb35ed271233ac8a916785'
tmdb.language = 'ko-KR'

# total
def get_recommendations(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores = list(enumerate(total[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:50]
    movie_indices = [i[0] for i in sim_scores]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

def get_recommendations_more(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores1 = list(enumerate(total[idx]))
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores1 = sim_scores1[13:50]
    movie_indices = [i[0] for i in sim_scores1]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

# credits
def get_recommendations1(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores = list(enumerate(credits[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:50]
    movie_indices = [i[0] for i in sim_scores]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

def get_recommendations_more1(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores1 = list(enumerate(credits[idx]))
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores1 = sim_scores1[13:50]
    movie_indices = [i[0] for i in sim_scores1]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

# overView
def get_recommendations2(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores = list(enumerate(overView[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:50]
    movie_indices = [i[0] for i in sim_scores]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

def get_recommendations_more2(title):
    idx = find_list[find_list['title'] == title].index[0]
    sim_scores1 = list(enumerate(overView[idx]))
    sim_scores1 = sorted(sim_scores1, key=lambda x: x[1], reverse=True)
    sim_scores1 = sim_scores1[13:50]
    movie_indices = [i[0] for i in sim_scores1]
    images = []
    titles = []
    for i in movie_indices:
        id = find_list['id'].iloc[i]
        details = movie.details(id)
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    return images, titles

st.set_page_config(layout='wide')

image_width=300
st.write(" ")
st.header(" ")
movie_list = find_list['title'].values
title = st.selectbox('Choose a movie you like', movie_list)

selectbox = st.selectbox(" ", [" 추 천 방 식 "," 추천 "," 정보 추천 ", " 줄거리 추천 "])

if selectbox == " 관련 추천 ": # total 사용
    con = st.container()
    con.caption("SELECT MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)                    
    if title:
        movie_details = movie.search(title)
        if movie_details:
            image_width = 300
            st.image('https://image.tmdb.org/t/p/w500' + movie_details[0]['poster_path'], image_width, use_column_width=False)
            st.write(title)
        else:
            st.write('Movie not found.')
    con = st.container()
    con.caption("RECOMMEND MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations(title)
        idx = 0
        for i in range(0, 2):
            cols = st.columns(6)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
    st.write(" ")
    st.write(" ")
    if st.button(" You wan't more? "):
        con = st.container()
        con.caption(" MORE RECOMMEND MOVIE")
        with st.spinner('Please wait...'):
            images, titles = get_recommendations_more(title)
            idx = 0
            for i in range(0, 2):
                cols = st.columns(5)
                for col in cols:
                    col.image(images[idx])
                    col.write(titles[idx])
                    idx += 1
    

if selectbox == " 정보 추천 ": # credits 사용
    con = st.container()
    con.caption("SELECT MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations1(title)                    
    if title:
        movie_details = movie.search(title)
        if movie_details:
            image_width = 300
            st.image('https://image.tmdb.org/t/p/w500' + movie_details[0]['poster_path'], image_width, use_column_width=False)
            st.write(title)
        else:
            st.write('Movie not found.')
    con = st.container()
    con.caption("RECOMMEND MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations1(title)
        idx = 0
        for i in range(0, 2):
            cols = st.columns(6)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
    st.write(" ")
    st.write(" ")
    if st.button(" You wan't more? "):
        con = st.container()
        con.caption(" MORE RECOMMEND MOVIE")
        with st.spinner('Please wait...'):
            images, titles = get_recommendations_more1(title)
            idx = 0
            for i in range(0, 2):
                cols = st.columns(5)
                for col in cols:
                    col.image(images[idx])
                    col.write(titles[idx])
                    idx += 1

if selectbox == " 줄거리 추천 ": #overView 사용
    con = st.container()
    con.caption("SELECT MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations2(title)                    
    if title:
        movie_details = movie.search(title)
        if movie_details:
            image_width = 300
            st.image('https://image.tmdb.org/t/p/w500' + movie_details[0]['poster_path'], image_width, use_column_width=False)
            st.write(title)
        else:
            st.write('Movie not found.')
    con = st.container()
    con.caption("RECOMMEND MOVIE")
    with st.spinner('Please wait...'):
        images, titles = get_recommendations2(title)
        idx = 0
        for i in range(0, 2):
            cols = st.columns(6)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
    st.write(" ")
    st.write(" ")
    if st.button(" You wan't more? "):
        con = st.container()
        con.caption(" MORE RECOMMEND MOVIE")
        with st.spinner('Please wait...'):
            images, titles = get_recommendations_more2(title)
            idx = 0
            for i in range(0, 2):
                cols = st.columns(5)
                for col in cols:
                    col.image(images[idx])
                    col.write(titles[idx])
                    idx += 1

