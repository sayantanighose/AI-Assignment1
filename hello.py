import streamlit as st
st.write("Hello world - Testing GIT")
X = st.text_input("What's your name?")
st.write ("Hello", X)
st.write("Choose the car you want to buy")
import pandas as pd
data = pd.read_csv("E:\My Programs\Data\carprices.csv")
st.write(data)
import numpy as np
#chart_data = pd.DataFrame(
#    np.random.randn(20,3), columns= ["a","b","c"])
chart_data = pd.DataFrame(data[["Mileage", "Sell Price($)"]].copy())
#st.write(chart_data)
st.bar_chart(chart_data, x = "Mileage", y = "Sell Price($)")
st.line_chart(chart_data)

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.title("This is a title", help="This is title help")
st.title("_Streamlit_ is :blue[cool] :sunglasses:", anchor= "COOL")

def get_user_name():
    return X

# ------------------------------------------------
# Want people to see this part of the code...

def get_punctuation():
    return '!!!'

greeting = "Hi there, "
user_name = get_user_name()
punctuation = get_punctuation()

st.write(greeting, user_name, punctuation)

# ...up to here
# ------------------------------------------------

foo = 'bar'
st.write('Done!')