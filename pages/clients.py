import main
import streamlit as st
import plotly.express as px


data = main.load_data()

st.sidebar.subheader("📞 Call Us ")
st.sidebar.markdown("01050605580")
st.sidebar.markdown("📧 eng.omarfathy98697@gmail.com")


list_of_names = [name for name in data["Name"].unique()]

def make_clinet(num_of_clinet, client):
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("photo.jpg", width=100)
        with col2:
            st.markdown(f"<h1 style'text-align: right; color: red;'>{num_of_clinet}.{client}</h1>",
                        unsafe_allow_html=True)

    st.dataframe(data[data["Name"] == client], width=1000)
    fig = px.scatter(data[data["Name"] == client], x='BPM', y='SpO2', title='BPM vs SpO2')

    st.plotly_chart(fig)
    st.image("gif.gif")

for num in range(len(list_of_names)):
    make_clinet(num+1, list_of_names[num])



