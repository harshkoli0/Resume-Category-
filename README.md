📄 Resume Analyzer (DL + Streamlit)

An interactive Resume Analysis System built using Deep Learning, NLP, and Streamlit.
This application allows users to paste resume text directly and automatically:

✔ Predict the Job Category using TF-IDF + LSTM
✔ Extract the Technical Skills section
✔ Display character count, word count, and unique words
✔ Clean and preprocess resume text
✔ Provide an easy-to-use Streamlit interface

🚀 Features
🔍 1. Resume Category Prediction (Deep Learning)

TF-IDF feature extraction

LSTM-based multi-class classification

Supports 20+ job categories
(Data Science, Python Developer, HR, Java Developer, Web Developer, DevOps, Testing, etc.)

Model files included:

resume_lstm_model.h5

tfidf_vectorizer.pkl

label_encoder.pkl

🛠 2. Technical Skills Section Extraction

Automatically extracts ONLY the skills section by detecting headings like:

Technical Skills

Skills

Tech Stack

Core Competencies

Areas of Expertise

✔ No PDF/DOCX text extractors
✔ Works directly on plain text input
✔ Fast regex-based extraction

📊 3. Resume Text Analysis

The app provides quick resume insights:

Total character count

Total word count

Total unique words

Cleaned resume preview

