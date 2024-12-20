import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def load_data():
    df = pd.read_csv("clients_data.csv")
    df.columns = ["Name", "BPM", "SpO2", "Humidity", "Temp_C", "Temp_F"]
    df["time"] = None
    return df


data = load_data()

st.sidebar.subheader("📞 Call Us ")
st.sidebar.markdown("01050605580")
st.sidebar.markdown("📧 eng.omarfathy98697@gmail.com")

list_of_names = [name for name in data["Name"].unique()]


def make_client(num_of_client, client):
    client_data = data[data["Name"] == client]
    client_data["time"] = [i + 1 for i in range(len(client_data))]
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image("photo.jpg", width=100)
        with col2:
            st.markdown(f"<h1 style's-align: right; color: red;'>{num_of_client}.{client}</h1>",
                        unsafe_allow_html=True)

    st.dataframe(client_data, width=1000)
    fig = make_subplots(
        rows=3, cols=1,
        subplot_titles=("BPM and SpO2", "Humidity", "Temperature (°C and °F)"),
        shared_xaxes=True
    )

    # Add BPM and SpO2 to the first subplot
    fig.add_trace(
        go.Scatter(x=client_data['time'], y=client_data['BPM'], mode='lines+markers', name='BPM',
                   line=dict(color='blue')),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=client_data['time'], y=client_data['SpO2'], mode='lines+markers', name='SpO2',
                   line=dict(color='green')),
        row=1, col=1
    )

    # Add Humidity to the second subplot
    fig.add_trace(
        go.Scatter(x=client_data['time'], y=client_data['Humidity'], mode='lines+markers', name='Humidity',
                   line=dict(color='purple')),
        row=2, col=1
    )

    # Add Temperature (Celsius and Fahrenheit) to the third subplot
    fig.add_trace(
        go.Scatter(x=client_data['time'], y=client_data['Temp_C'], mode='lines+markers', name='Temp (°C)',
                   line=dict(color='red')),
        row=3, col=1
    )
    fig.add_trace(
        go.Scatter(x=client_data['time'], y=client_data['Temp_F'], mode='lines+markers', name='Temp (°F)',
                   line=dict(color='orange')),
        row=3, col=1
    )

    # Update layout
    fig.update_layout(
        title_text="BPM, SpO2, Humidity, and Temperature Trends",
        height=800,
        showlegend=True
    )

    # Show the plot

    st.plotly_chart(fig)

    st.image("gif.gif")


for num in range(len(list_of_names)):
    make_client(num + 1, list_of_names[num])
