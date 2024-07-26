import streamlit as st
import pickle 
import numpy as np

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
st.header('Some example')
col1, col2, col3 = st.columns(3)

# Add tables to each column
with col1:
    st.table([
        ["Sepal Length: 5.1 cm"],
        ["Sepal Width: 3.5 cm"],
        ["Petal Length: 1.4 cm"],
        ["Petal Width: 0.2 cm"],
        ["Species: Setosa"]
    ])

with col2:
    st.table([
        ["Sepal Length: 7.0 cm"],
        ["Sepal Width: 3.2 cm"],
        ["Petal Length: 4.7 cm"],
        ["Petal Width: 1.4 cm"],
        ["Species: Versicolor"]
    ])
with col3:
    st.table([
        ["Sepal Length: 6.3 cm"],
        ["Sepal Width: 3.3 cm"],
        ["Petal Length: 6.0 cm"],
        ["Petal Width: 2.5 cm"],
        ["Species: Verginica"]
    ])


st.title('Iris Specis prediction')

sep_len =st.number_input('sepal length' , min_value=0.0, max_value=10.0,step=0.1)
sep_width =st.number_input('sepal width' , min_value=0.0, max_value=10.0,step=0.1)
petal_len =st.number_input('petal length' , min_value=0.0, max_value=10.0,step=0.1)
petal_width =st.number_input('petal width' , min_value=0.0, max_value=10.0,step=0.1)

target =['setosa','versicolor','virginica']


button_style = """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;  /* Green */
        color: white;
        height: 3em;
        width: 10em;
        border-radius: 10px;
        border: none;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #45a049;  /* Darker green */
    }
    </style>
    """

st.markdown(button_style, unsafe_allow_html=True)

if st.button('Model Answer'):
    input_data = np.array([[sep_len , sep_width ,petal_len , petal_width]])

    prediction = model.predict(input_data)[0]
    st.write(f"It is {(target[prediction]).upper()} species flower")
