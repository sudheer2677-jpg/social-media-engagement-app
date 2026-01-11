📊 Social Media Engagement Predictor

A machine learning–powered **Streamlit web application** that predicts social media engagement based on post timing, sentiment, platform, and content type.

🔗 **Live App:**  [
https://social-media-engagement-app-jimx7lj3rrnxes9erwfqtp.streamlit.app/
---

## 🚀 Features
- Predicts engagement score for social media posts
- Interactive UI built with **Streamlit**
- Uses a trained **Machine Learning regression model**
- Real-time predictions
- Clean and user-friendly interface

---

## 🧠 Machine Learning Model
- Model Type: Regression model (trained using scikit-learn)
- Preprocessing: Feature scaling using `StandardScaler`
- Model & scaler serialized using `joblib`

---

## 📥 Input Features
| Feature | Description |
|------|-----------|
| Post Hour | Hour of posting (0–23) |
| Post Day | Day of month |
| Day of Week | 0 (Mon) – 6 (Sun) |
| Sentiment Score | Range from -1 to 1 |
| Number of Hashtags | Count of hashtags |
| Platform | Twitter / Instagram |
| Post Type | Video / Image / Text / Poll |

---

## 🖥️ Tech Stack
- **Python**
- **Streamlit**
- **NumPy**
- **scikit-learn**
- **joblib**
- **GitHub**
- **Streamlit Cloud**

---

## 📂 Project Structure
