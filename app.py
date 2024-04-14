import streamlit as st
from function import load_data, data_distribution, relation, composition, comparison, predict_cluster, data_storytelling
from streamlit_option_menu import option_menu


with st.sidebar:

    selected = st.selectbox("Student Alcohol Consumption", ["Home", "Data Visualization", "Predict"])

    if selected == "Data Visualization":
        pilih = option_menu(
        menu_title="", 
        options=["Data Distribution", "Relation", "Composition", "Comparison"],
        default_index=0)

def display_Home():
    df = load_data()
    # st.write(df)
    data_storytelling(df)

def display_data_distribution():
    df = load_data()
    data_distribution(df)

def display_relation():
    df = load_data()
    relation(df)

def display_composition():
    df = load_data()
    composition(df)

def display_comparison():
    df = load_data()
    comparison(df)

def display_prediction():
    predict_cluster()


if selected == "Home":
    display_Home()
elif selected == "Data Visualization":
    if pilih == "Data Distribution":
        display_data_distribution()
    elif pilih == "Relation":
        display_relation()
    elif pilih == "Composition":
        display_composition()
    elif pilih == "Comparison":
        display_comparison()
    
elif selected == "Predict":
    display_prediction()
