import numpy as np
import pandas as pd
import streamlit as st
import pickle
import requests


def recommend(book):
    with open('final_rating.pkl', 'rb') as file:
        popular = pickle.load(file)

    books_dict = pickle.load(open('books_dict.pkl', 'rb'))
    books = pd.DataFrame(books_dict)

    bt = pickle.load(open('bt.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    index = np.where(bt.index == title)[0][0]
    similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:20]
    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['title'] == bt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('title')['title']))
        item.extend(list(temp_df.drop_duplicates('title')['author']))
        item.extend(list(temp_df.drop_duplicates('title')['Image-URL-M']))

        data.append(item)
    return data


books_dict = pickle.load(open('books_dict.pkl', 'rb'))
books = pd.DataFrame(books_dict)

st.title('book recommender system')
selected_book_name = st.selectbox(
    'Welcome to the Library',
    books['title'].values,
    index=0  # Set the default selection index
)


selected_book_info = books[books['title'] == selected_book_name]

# Display book information
st.write(f"Selected Book: {selected_book_info['title'].values[0]}")
st.write(f"Author: {selected_book_info['author'].values[0]}")

if st.button('recommend'):
    title , author = recommend(selected_book_info)


    col1, col2, col3, col4, col5 ,col6, col7, col8, col9, col10,col11, col12, col13, col14, col15,col16, col17, col18, col19, col20 = st.columns(20)

    with col1:
        st.text(title[0])
        st.text(author[0])

    with col2:
        st.text(title[1])
        st.text(author[1])

    with col3:
        st.text(title[2])
        st.text(author[2])

    with col4:
        st.text(title[3])
        st.text(author[3])

    with col5:
        st.text(title[4])
        st.text(author[4])

    with col6:
        st.text(title[5])
        st.text(author[5])

    with col7:
        st.text(title[6])
        st.text(author[6])

    with col8:
        st.text(title[7])
        st.text(author[7])

    with col9:
        st.text(title[8])
        st.text(author[8])

    with col10:
        st.text(title[9])
        st.text(author[9])

    with col11:
        st.text(title[10])
        st.text(author[10])

    with col12:
        st.text(title[11])
        st.text(author[11])

    with col13:
        st.text(title[12])
        st.text(author[12])

    with col14:
        st.text(title[13])
        st.text(author[13])

    with col15:
        st.text(title[14])
        st.text(author[14])

    with col16:
        st.text(title[15])
        st.text(author[15])

    with col17:
        st.text(title[16])
        st.text(author[16])

    with col18:
        st.text(title[17])
        st.text(author[17])

    with col19:
        st.text(title[18])
        st.text(author[18])

    with col20:
        st.text(title[19])
        st.text(author[19])
