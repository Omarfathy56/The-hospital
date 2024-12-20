import pandas as pd
import streamlit as st


# @st.cache_data
def load_data():
    df = pd.read_csv("clients_data.csv")
    df.columns = ["Name", "BPM", "SpO2", "Humidity", "Temp_C", "Temp_F"]

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
        st.markdown("<h1 style's-align: right; color: red;'>Welcome to Local Health Organization</h1>",
                    unsafe_allow_html=True)

st.subheader("Welcome to LHO : ")
st.markdown("""
**Welcome to HealthSense – Your Partner in Wellness!**  
At HealthSense, we aim to empower individuals to monitor and maintain their health effortlessly. Our app provides real-time insights into your body's vital metrics, including:

- **Heart Rate (BPM):** Stay informed about your cardiovascular health.  
- **Oxygen Saturation (SpO2):** Ensure your body is getting the oxygen it needs.  
- **Body Temperature:** Track your body temperature in both °C and °F to detect potential health concerns early.  
- **Environmental Humidity and Temperature:** Understand your surroundings and their impact on your well-being.  

We are committed to making health monitoring accessible to everyone, helping you lead a healthier, more informed life. Together, let’s strive for a future where wellness is within everyone’s reach.  

**Your health, simplified.**
""")


st.write("Clients Data:")
st.dataframe(data, width=1000)


