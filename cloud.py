import streamlit as st
import requests

def get_weather(city):
    API_KEY = '3a05413ecf96bcd5c8654308b694cd13'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return {'temperature': temperature, 'humidity': humidity, 'description': description}
    else:
        return {'error': 'City not found.'}


st.title('Weather App')
city = st.text_input('Enter city name', '')
st.write(f"Selected city: {city}")
if st.button('Get Weather'):
    weather_data = get_weather(city)
    if 'error' in weather_data:
        st.error(weather_data['error'])
    else:        
        st.subheader('Weather Information')
        st.write(f"Temperature: {weather_data['temperature']}K")
        st.write(f"Humidity: {weather_data['humidity']}%")
        st.write(f"Description: {weather_data['description']}")


st.markdown(
    """
    <style>
        div.stButton > button:first-child {
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }

        div.stButton > button:first-child:hover {
            background-color: #45a049;
        }

        div.stTextInput > div > div > input {
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
    </style>
    """,
    unsafe_allow_html=True
)
