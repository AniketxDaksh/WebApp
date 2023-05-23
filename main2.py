import ssl
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from streamlit_lottie import st_lottie

import streamlit.components.v1 as components




# Mapping dictionaries
gender_map = {'Male': 1, 'Female': 0}
education_map = {'School': 0, 'Bachelor': 1, 'Masters': 2, 'PHD': 3}
yes_no_map = {'Yes': 1, 'No': 0}
alcohol_map = {'Excessive': 2, 'Moderate': 1, 'Never': 0}

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Define the URL or path of your CSV file
url = 'depression_level_2.csv'

# Load data
df = pd.read_csv(url)

try:
    df = pd.read_csv(url)
except Exception as e:
    st.error(f"Error loading data: {e}")
    raise e

# Handle missing values
df.drop("Unnamed: 0", axis=1, inplace=True)

# Split data into features and target
X = df.drop('Depression Status', axis=1)
y = df['Depression Status']

# Convert categorical variables to numerical using one-hot encoding
ohe = OneHotEncoder(sparse=False)
X_cat = X.select_dtypes(include=['object'])
X_num = X.select_dtypes(exclude=['object'])

X_cat_ohe = ohe.fit_transform(X_cat)
scaler = StandardScaler()
X_num_scaled = scaler.fit_transform(X_num)

X = np.concatenate([X_cat_ohe, X_num_scaled], axis=1)

# Train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Set the title and header of the app
st.title('DEPRESSION PREDICTION ')

# Load and display the Lottie animation
lottie_url = "https://assets4.lottiefiles.com/private_files/lf30_zzItmF.json"
lottie_json = requests.get(lottie_url).json()
st_lottie(lottie_json, speed=1, width=800, height=600)


# Add a toggler bar for Overview and User Guide
with st.expander("ℹ️ Overview"):
    st.write('Welcome to the Depression Prediction Web App! This web app is designed to help assess and predict the likelihood of depression based on various input features. By providing information about your age, gender, education, BMI, and other factors, the web app will generate a prediction and provide insights into your mental health.')

with st.expander("📚 User Guide"):
    st.write('To use this web app, follow these steps:')
    st.write('1. Fill in the required input fields in the sidebar, such as your age, gender, education, BMI, etc.')
    st.write('2. Click the "Submit" button.')
    st.write('3. The web app will generate a prediction regarding your depression status.')
    st.write('4. The prediction will be displayed, indicating whether you are at risk of depression or not.')
    st.write('5. Additionally, graphical reports visualizing your mental health journey will be shown, including a bar chart, scatter plot, and heatmap.')



# Improve sidebar layout
st.sidebar.title('Depression Prediction App')
st.sidebar.markdown('Enter the values below to predict depression status.')

# Define input fields
age = st.sidebar.number_input('Age', min_value=1, max_value=120, value=1)
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'], key='gender_select', index=st.session_state.get('gender_index', 0))
education = st.sidebar.selectbox('Education', ['School', 'Bachelor', 'Masters', 'PHD'], key='education_select', index=st.session_state.get('education_index', 0))
BMI = st.sidebar.number_input('BMI', min_value=0, max_value=100, value=1)
Past_History_of_Depression = st.sidebar.selectbox('Past_History_of_Depression', ['Yes', 'No'], key='past_depression_select', index=st.session_state.get('past_depression_index', 0))
Family_History_of_Depression = st.sidebar.selectbox('Family_History_of_Depression', ['Yes', 'No'], key='family_depression_select', index=st.session_state.get('family_depression_index', 0))
Sleep_Duration_hours = st.sidebar.number_input('Sleep_Duration_hours', min_value=0, max_value=24, value=3)
Physical_Activity_minutes = st.sidebar.number_input('Physical_Activity_minutes', min_value=0, max_value=3600,
                                                    value=1, key='physical_activity')
Alcohol_Consumption_drinks_per_week = st.sidebar.selectbox('Alcohol_Consumption_drinks_per_week',
                                                           ['Excessive', 'Moderate', 'Never'],
                                                           key='alcohol_consumption',
                                                           index=st.session_state.get('alcohol_index', 0))
Smoking_Status = st.sidebar.number_input('Smoking_Status', min_value=0, max_value=100, value=1,
                                         key='smoking_status')

# Update session state with the selected indexes
st.session_state.gender_index = st.session_state.gender_select.index(gender)
st.session_state.education_index = st.session_state.education_select.index(education)
st.session_state.past_depression_index = st.session_state.past_depression_select.index(Past_History_of_Depression)
st.session_state.family_depression_index = st.session_state.family_depression_select.index(Family_History_of_Depression)
st.session_state.alcohol_index = st.session_state.alcohol_consumption.index(Alcohol_Consumption_drinks_per_week)

# Submit button
submitted = st.button('Submit', key='submit_button')

if submitted:
    # Create input feature vector
    input_data = np.array([[age, gender_map[gender], education_map[education], BMI,
                            yes_no_map[Past_History_of_Depression], yes_no_map[Family_History_of_Depression],
                            Sleep_Duration_hours, Physical_Activity_minutes,
                            alcohol_map[Alcohol_Consumption_drinks_per_week],
                            Smoking_Status]], dtype='float64')

    # Make prediction using trained model
    prediction = model.predict(input_data)[0]

    # Define output
    st.write('### Prediction')
    if prediction > 50:
        st.warning('You are at risk of depression.')

        st.write('Prediction Score:', prediction)
        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_ls1v2j0r.json"
        lottie_json = requests.get(lottie_url).json()
        st.markdown('&nbsp;' * 10, unsafe_allow_html=True)
        st_lottie(lottie_json, speed=1, width=800, height=600)
    else:
        st.success('You are not at risk of depression.')

        st.write('Prediction Score:', prediction)
        lottie_url = "https://assets2.lottiefiles.com/packages/lf20_gmspxrnd.json"
        lottie_json = requests.get(lottie_url).json()
        st.markdown('&nbsp;' * 10, unsafe_allow_html=True)
        st_lottie(lottie_json, speed=1, width=800, height=600)

    # Plotting
    st.write('### Graphical Reports: Visualizing Your Mental Health Journey')

    # Bar chart
    st.write('#### Bar Chart')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=df, x='Physical Activity (minutes)', ax=ax)
    ax.set_title('Physical Activity (minutes)')
    st.pyplot(fig)

    # Scatter plot
    st.write('#### Scatter Plot')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.scatterplot(data=df, x='Sleep Duration (hours)', y='Physical Activity (minutes)', ax=ax)
    ax.set_title('Sleep Duration vs Physical Activity')
    st.pyplot(fig)

    # Heatmap
    st.write('#### Heatmap')
    fig, ax = plt.subplots(figsize=(10, 5))
    correlation = df.corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
