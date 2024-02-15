
import streamlit as st
import pandas as pd

st.title('My Title')
st.title('Another :blue[Blue Title] :sunglasses:')
st.header('My Header')
st.text('🥑🍞 Some text')
st.text('🥣 texts')
st.text('🥗 text')
st.text('🐔 text')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)

