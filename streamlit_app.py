
import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError



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
st.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

# call fruityvice API (does not require key)
st.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = st.text_input('What fruit would you like information about?')  # ,'Kiwi'
    if not fruit_choice:
        st.error('Please select a fruit to get information.')
    else:
        st.dataframe(get_fruityvice_data(fruit_choice))

except URLError as e:
    st.error()


# my_datagov_api_key = 'm9q3NAYhygSJDZhdELVIxChsgVgMNi2a7AM9DdLS'
# fruit_choice_datagov = st.text_input('Search food data from US Department of Agriculture FoodData Central')
# st.write('The user entered', fruit_choice_datagov, '. Searching US Department of Agriculture FoodData Central dataset')
# datagov_response = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search' + fruit_choice)

# st.text()


st.header('The fruit load list contains:')
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        # my_cur.execute('SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()')
        # return my_cur.fetchone()
        my_cur.execute('SELECT * from fruit_load_list')
        return my_cur.fetchall()

# add a button to load fruit list
if st.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**st.secrets['snowflake'])
    my_data_row = get_fruit_load_list()
    st.dataframe(my_data_row)


# add multiselect
st.header('You can add a fruit to the list')
add_my_fruit = st.text_input('What fruit would you like to add?')
st.write('The user added fruit:', add_my_fruit)

st.stop()
my_cur.execute(f"insert into fruit_load_list values ({add_my_fruit})")
my_data_row = my_cur.fetchall()
st.dataframe(my_data_row)