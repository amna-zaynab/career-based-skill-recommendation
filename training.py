import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\aavan\OneDrive\Desktop\Final_Corrected_Career_Skills_Dataset.csv")

# Combine all skill columns into a single text field
skill_columns = [col for col in df.columns if col.startswith('skill')]
df['Skills'] = df[skill_columns].apply(lambda row: ' '.join(row.dropna().astype(str)), axis=1)

# Encode the career labels
label_encoder = LabelEncoder()
df['Career'] = label_encoder.fit_transform(df['Career'])

# Split the data into features and labels
X = df['Skills']
y = df['Career']

# Tokenize the text data
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(X)
X_seq = tokenizer.texts_to_sequences(X)
X_pad = pad_sequences(X_seq, maxlen=100)

# Save the Tokenizer
with open(r"C:\Users\aavan\OneDrive\Desktop\new mini\tokenizer.pkl", 'wb') as f:
    pickle.dump(tokenizer, f)
print("Tokenizer file saved successfully.")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_pad, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Embedding(input_dim=10000, output_dim=128, input_length=100, name="embedding_layer"))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Define callbacks
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=3, min_lr=0.0001)
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model
history = model.fit(X_train, y_train,
                    epochs=20,
                    batch_size=64,
                    validation_data=(X_test, y_test),
                    callbacks=[reduce_lr, early_stopping])

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Loss: {loss:.4f}')
print(f'Test Accuracy: {accuracy * 100:.2f}%')

# Generate predictions
y_pred = model.predict(X_test).argmax(axis=1)

# Classification Report
print(classification_report(y_test, y_pred, labels=np.unique(y_test)))

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred, labels=np.unique(y_test))
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', fmt='d', xticklabels=np.unique(y_test), yticklabels=np.unique(y_test))
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Save the model
model.save(r"C:\Users\aavan\OneDrive\Desktop\new mini\career_lstm_model.h5")
print("Model saved successfully.")  