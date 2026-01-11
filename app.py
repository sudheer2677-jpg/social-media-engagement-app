import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load("engagement_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📊 Social Media Engagement Predictor")

st.write("Enter post details to predict engagement")

# User inputs
hour = st.slider("Post Hour (0–23)", 0, 23, 12)
post_day = st.selectbox("Post Day", [0,1,2,3,4,5,6])
day_of_week = st.selectbox("Day of Week", [0,1,2,3,4,5,6])
sentiment_score = st.slider("Sentiment Score", -1.0, 1.0, 0.0)
hashtags = st.slider("Number of Hashtags", 0, 20, 5)

platform_twitter = st.selectbox("Platform Twitter?", [0, 1])
platform_instagram = st.selectbox("Platform Instagram?", [0, 1])

post_type_video = st.selectbox("Post Type Video?", [0, 1])
post_type_poll = st.selectbox("Post Type Poll?", [0, 1])
post_type_image = st.selectbox("Post Type Image?", [0, 1])
post_type_text = st.selectbox("Post Type Text?", [0, 1])

# Arrange input in correct order
input_data = np.array([[  
    post_day,
    sentiment_score,
    hashtags,
    hour,
    day_of_week,
    platform_instagram,
    platform_twitter,
    post_type_image,
    post_type_poll,
    post_type_text,
    post_type_video
]])

# Scale input
scaled_input = scaler.transform(input_data)

# Predict
if st.button("Predict Engagement"):
    prediction = model.predict(scaled_input)
    st.success(f"📈 Predicted Engagement Score: {prediction[0]:.2f}")
