import numpy as np
import pandas as pd
import streamlit as st
import pickle

def recommend(selected_book_name, books):
    bt = pickle.load(open('bt.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # Check if selected_book_name exists in the index
    if selected_book_name not in bt.index:
        st.warning(f"Book with title '{selected_book_name}' not found in the dataset.")
        return []

    index = np.where(bt.index == selected_book_name)[0][0]
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

with open('final_rating.pkl', 'rb') as file:
    popular = pickle.load(file)

selected_book_info = books[books['title'] == selected_book_name]

# Display book information
st.write(f"Selected Book: {selected_book_info['title'].values[0]}")
st.write(f"Author: {selected_book_info['author'].values[0]}")

if st.button('recommend'):
    recommendations = recommend(selected_book_name, books)

    # Display recommendations
    for i, (title, author, image_url) in enumerate(recommendations):
        col1, col2, col3 = st.columns([1, 1, 2])
        with col1:
            st.image(image_url, caption=f"{title} - {author}", use_column_width=True)
        with col2:
            st.text(title)
            st.text(author)
        with col3:
            st.text(f"Recommendation {i + 1}")
