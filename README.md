# 🧠 Resume Analyzer (DL + Streamlit)

A complete Resume Analysis system built using Machine Learning, NLP, and Streamlit.
This application allows users to paste or input raw resume text directly and automatically:

✔ Predict the **Job Category** using TF-IDF + LSTM  
✔ Extract the **Technical Skills Section**  
✔ Display **character count**, **word count**, and **unique words**  
✔ Clean and preprocess resume text  
✔ Provide a simple and interactive interface using Streamlit  

---

🌐 Live App

👉 Try it here:

🔗 https://resume-category-git-mpqyjcdxpgwsxvpxs2v3np.streamlit.app/

---
## 🚀 Features

### 🔍 1. Resume Category Prediction (Machine Learning)
- TF-IDF feature extraction  
- LSTM-based multi-class classification  
- Supports 20+ resume categories (Data Science, HR, Web Developer, DevOps, etc.)
- Model files included:
  - `resume_lstm_model.h5`
  - `tfidf_vectorizer.pkl`
  - `label_encoder.pkl`

---

### 🛠 2. Technical Skills Section Extraction
Automatically extracts the section containing skills by detecting headings such as:

- **Technical Skills**
- **Skills**
- **Tech Stack**
- **Core Competencies**
- **Areas of Expertise**

Outputs the exact skill block from the resume.

---

### 📊 3. Resume Text Analysis
- Character count  
- Word count  
- Unique words  
- Cleaned text preview  

---



