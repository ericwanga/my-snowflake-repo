
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

# load data as df
my_fruit_df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_df = my_fruit_df.set_index('Fruit')

# add multiselect, set 2 fruits as default selection
fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_df.index), ['Avocado', 'Strawberries'])
st.text('dtype: ', type(fruits_selected))
# filter df with selected fruits
fruits_to_show = my_fruit_list.loc[fruits_selected]

# display
# st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)

