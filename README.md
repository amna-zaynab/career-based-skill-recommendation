# 💡 Career-Based Skill Recommendation System  

An **AI-Powered Skill Roadmap Generator** that helps students and professionals identify the exact skills they need to learn to achieve their **career goals** — and generates a **personalized learning roadmap** excluding already acquired skills. 🚀

---

---

## 🧩 Overview

The **Career-Based Skill Recommendation System** predicts the essential skills required for any chosen career path using **deep learning (LSTM)**.  
It allows users to input:
- Their **desired career** (e.g., *Data Scientist*, *Full-Stack Developer*, *Business Analyst*), and  
- The **skills they already have**  

The system then:
✅ Predicts the additional skills required  
✅ Generates a **personalized learning roadmap**  
✅ Optionally provides **course recommendations** (planned)  

---

## ⚙️ Features

- 🔍 **Career-to-Skill Prediction:** Uses an LSTM model to predict the skill set needed for a given career.  
- 🧠 **AI-Powered Recommendations:** Learns from existing career–skill mappings.  
- 🧾 **Personalized Roadmap:** Removes already-acquired skills to show only missing ones.  
- 🧩 **RESTful API (Flask):** For easy integration with web apps or mobile clients.  
- 💾 **SQLite Database:** To store user data, skills, and roadmaps.  
- 🖥️ **Simple Frontend:** HTML/CSS/JS pages for interaction (if included).  
- 📈 **Model Accuracy:** ~95.7% skill prediction accuracy.  

---

## 🎯 Motivation

Many learners struggle to answer questions like:
> *“What skills should I learn next for my dream career?”*  
> *“Am I focusing on the right tools and technologies?”*

This project was developed to help answer these questions automatically using **Machine Learning** — by mapping careers to skills based on real-world data.

It combines your knowledge in **AI, Flask, TensorFlow, and Front-End Development** to build a practical and intelligent career guidance platform.

---

## 🧠 Architecture


---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask, Python |
| **Database** | SQLite |
| **ML Framework** | TensorFlow / Keras |
| **Model Type** | LSTM Neural Network |
| **Data Preprocessing** | Tokenization, Padding |
| **API Communication** | JSON over HTTP |
| **Tools** | VS Code, Git, GitHub |

---

## 🚀 Getting Started

### 🧾 Prerequisites
- Python 3.x  
- pip (Python package manager)  
- Virtual environment (recommended)  

---

## career-based-skill-recommendation/
```
│
├── app.py                    # Flask backend entry point
├── training.py               # Script to train LSTM model
├── career_lstm_model.h5      # Trained model file
├── tokenizer.pkl             # Tokenizer object
├── requirements.txt          # Required packages
│
├── static/                   # (Optional) Frontend static files (CSS/JS)
├── templates/                # (Optional) HTML templates for UI
│
└── README.md                 # This file
```

### 📦 Installation

# Clone the repository
git clone https://github.com/amna-zaynab/career-based-skill-recommendation.git
cd career-based-skill-recommendation

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
