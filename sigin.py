import streamlit as st

def main():
    st.set_page_config(
        page_title="Depression Prediction Web App - Signup",
        page_icon="🔒",
        layout="centered"  # Center align the content
    )

    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to bottom, #98240C, #0B63B0);
            }
            .container {
                max-width: 500px;
                background-color: #ffffff;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                padding: 50px;
                color: #000000;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center; color: #ffffff;'>Depression Prediction WebApp</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #ffffff;'>Signup</h2>", unsafe_allow_html=True)

    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")

    if st.button("Sign Up"):
        st.success("Thank you for signing up!")
        st.markdown("<p style='text-align: center;'>Redirecting to the next page...</p>", unsafe_allow_html=True)
        redirect_link = "https://aniketxdaksh-webapp-main2-7tja2p.streamlit.app/"
        st.write(f'<meta http-equiv="refresh" content="3;URL={redirect_link}">', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
