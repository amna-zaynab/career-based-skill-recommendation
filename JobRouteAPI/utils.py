from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MODEL_PATH = r"C:\Users\aavan\OneDrive\Desktop\new mini\career_lstm_model.h5"
TOKENIZER_PATH = r"C:\Users\aavan\OneDrive\Desktop\new mini\tokenizer.pkl"

# Career ID to Career Name Mapping
career_mapping = {
    0: "Data Scientist",
    1: "Web Developer",
    2: "Software Engineer",
    3: "AI Engineer",
    4: "Backend Developer",
    5: "Frontend Developer",
    6: "Machine Learning Engineer",
    7: "Cyber Security Specialist",
    8: "Full Stack Developer",
    9: "Cloud Engineer"
}

try:
    model = load_model(MODEL_PATH, compile=True)
    if model:
        print("Model Loaded Successfully")
        model.summary()  # Print model summary for verification
except Exception as e:
    print(f"Error loading model: {e}")
    model = None  # Ensure model is defined even if loading fails

try:
    with open(TOKENIZER_PATH, "rb") as handle:
        tokenizer = pickle.load(handle)
        print("Tokenizer Loaded Successfully")
except FileNotFoundError:
    print("Tokenizer file not found")
except Exception as e:
    print(f"Error loading tokenizer: {e}")


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=1)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.JWTError:
        return None

def predict_career(skill_text):
    try:
        if model is None:
            raise Exception("Model is not loaded correctly")
        skill_text = skill_text.lower()  # Lowercase the input
        seq = tokenizer.texts_to_sequences([skill_text])
        print(f"Tokenized Sequence: {seq}")  # Log the tokenized sequence
        padded_seq = pad_sequences(seq, maxlen=100)
        print(f"Padded Sequence: {padded_seq}")  # Log the padded sequence
        prediction = model.predict(padded_seq)
        result = np.argmax(prediction, axis=1)[0]
        career_name = career_mapping.get(int(result), "Unknown Career")
        return career_name
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None
