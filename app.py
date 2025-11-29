import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ----------------------------
# Load trained model and components
# ----------------------------

model = load_model("resume_lstm_model.h5")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

# Your cleaning function
def cleanResume(resume_text):
    import re
    resume_text = re.sub('http\S+\s*', ' ', resume_text)
    resume_text = re.sub('RT|cc', ' ', resume_text)
    resume_text = re.sub('#\S+', '', resume_text)
    resume_text = re.sub('@\S+', '  ', resume_text)
    resume_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resume_text)
    resume_text = re.sub(r'[^\x00-\x7f]', ' ', resume_text)
    resume_text = re.sub('\s+', ' ', resume_text)
    return resume_text

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("📄 Resume Category Classifier (LSTM + TF-IDF)")
st.write("Upload your resume text and get predicted job category.")

resume_input = st.text_area("Paste your resume text here:", height=250)

if st.button("Predict Category"):
    if len(resume_input.strip()) == 0:
        st.warning("Please enter the resume text.")
    else:
        # clean text
        cleaned = cleanResume(resume_input)

        # transform using TF-IDF
        features = vectorizer.transform([cleaned])
        dense = features.toarray()

        reshaped = np.reshape(dense, (1, 1, dense.shape[1]))

        # predict
        prediction = model.predict(reshaped)
        pred_index = np.argmax(prediction)

        # decode label
        category = label_encoder.inverse_transform([pred_index])[0]

        st.success(f"### 🏆 Predicted Category: **{category}**")
