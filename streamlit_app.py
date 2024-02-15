
import streamlit as st
import pandas as pd


st.title('New Healthy Diner')
st.title('Healthy :green[breakfast favorites] :sunglasses:')
st.header('Breakfast Favorites')
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


# my_datagov_api_key = 'm9q3NAYhygSJDZhdELVIxChsgVgMNi2a7AM9DdLS'
# fruit_choice_datagov = st.text_input('Search food data from US Department of Agriculture FoodData Central')
# st.write('The user entered', fruit_choice_datagov, '. Searching US Department of Agriculture FoodData Central dataset')
# datagov_response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search' + fruit_choice)

# st.text()

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets['snowflake'])
my_cur = my_cnx.cursor()
# my_cur.execute('SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()')
# my_data_row = my_cur.fetchone()
my_cur.execute('SELECT * from fruit_load_list')
my_data_row = my_cur.fetchall()
st.header('The fruit load list contains:')
st.dataframe(my_data_row)