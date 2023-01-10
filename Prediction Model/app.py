import pandas as pd
import numpy as np
import pickle
import streamlit as st

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
model = pickle.load(pickle_in)

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(Open, High, Low, Close):
    prediction = model.predict([[Open, High, Low, Close]])
    print(prediction)
    return prediction

# this is the main function in which we define our webpage
def main():
    st.title("BTC Prediction")

    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Bitcoin Prediction </h1>
    </div>
    """

    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)

    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    Open = st.text_input("Open", "Type Here")
    High = st.text_input("High", "Type Here")
    Low = st.text_input("Low", "Type Here")
    Close = st.text_input("Close", "Type Here")
    result =""

    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(Open,High,Low,Close)
    st.success('The output is {}'.format(result))

if __name__=='__main__':
    main()
