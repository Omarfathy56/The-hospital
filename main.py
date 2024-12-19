import pandas as pd
import streamlit as st


# @st.cache_data
def load_data():
    df = pd.read_csv("clients_data.csv")
    df.columns = ["Name", "BPM", "SpO2"]
    return df


data = load_data()

st.sidebar.subheader("📞 Call Us ")
st.sidebar.markdown("01050605580")
st.sidebar.markdown("📧 eng.omarfathy98697@gmail.com")


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("LHO.webp", width=500)
    with col2:
        st.markdown("<h1 style'text-align: right; color: red;'>Welcome to Local Health Organization</h1>",
                    unsafe_allow_html=True)

st.subheader("Welcome to LHO : ")
st.markdown("we here help people to measure their heart rate state ,O2 and temperature in their body , \n we hope we "
            "will be useful to all people and help them as far as possible ")


st.write("Clients Data:")
st.dataframe(data, width=1000)


