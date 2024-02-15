
import streamlit as st
import pandas as pd


st.title('My Title')
st.title('Another :blue[Blue Title] :sunglasses:')
st.header('My Header')
st.text('🥑🍞 Avocado Toast')
st.text('🥣 Kale, Spinach & Rocket Smoothie')
st.text('🥗 Omega 3 & Blueberry Oatmeal')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# load data as df
my_fruit_df = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_df = my_fruit_df.set_index('Fruit')

# add multiselect, set 2 fruits as default selection
fruits_selected = st.multiselect('Pick some fruits:', list(my_fruit_df.index), ['Avocado', 'Strawberries'])

# filter df with selected fruits
fruits_to_show = my_fruit_df.loc[fruits_selected]

# st.dataframe(my_fruit_list)
st.dataframe(fruits_to_show)

# call fruityvice API (does not require key)
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)


import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)

# st.text(fruityvice_response.json())
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)
