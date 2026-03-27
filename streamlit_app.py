import streamlit as st 
import requests
st.title("Placement Predictor")
cgpa=st.slider("CGPA",0.0,10.0,7.0)
aptitude=st.slider("Aptitude score",0,100,70)
communication=st.slider("communication",1,10,5)
projects=st.slider("Projects",0,5,2)
if st.button("predict"):
    url="http://127.0.0.1:5000/predict"
    data={
        "cgpa":cgpa,
        "aptitude":aptitude,
        "communication":communication,
        "projects":projects
    }
    response=requests.post(url,json=data)
    result=response.json()
    if result['prediction']==1:
        st.success("you will be placed!")
    else:
        st.error("not likely to be placed")