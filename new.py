import streamlit as st
import requests
from streamlit_lottie import st_lottie

def main():
    st.set_page_config(
        page_title="Depression Prediction Web App - Login",
        page_icon="🔒",
        layout="wide",  # Update the layout to "wide"
        initial_sidebar_state="collapsed"
    )

    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to bottom, #98240C, #0B63B0);
                display: flex; /* Add flex display */
                justify-content: center; /* Center align horizontally */
                align-items: center; /* Center align vertically */
                height: 100vh; /* Set the height to fill the viewport */
            }
            .container {
                max-width: 500px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                padding: 100px;
                color: #000000;
            }
        </style>
        """,
        unsafe_allow_html=True
    )



    st.markdown("<h1 style='text-align: center; color: #ffffff;'>Depression Prediction WebApp</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ffffff;'>Login</h2>", unsafe_allow_html=True)

    name = st.text_input("Name:")
    gender = st.text_input("Gender:")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if st.button("Submit"):
        st.success("Thank you for submitting the form!")
        st.markdown("<p style='text-align: center;'>Redirecting to the next page...</p>", unsafe_allow_html=True)
        redirect_link = "https://dpc4.carrd.co"
        st.write(f'<meta http-equiv="refresh" content="3;URL={redirect_link}">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

