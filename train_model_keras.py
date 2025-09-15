import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
import joblib

# 1. Cargar dataset
data = pd.read_csv("dataset.csv")

# 2. Separar features (X) y labels (y)
X = data.drop("label", axis=1).values
y = data["label"].values

# 3. Convertir letras a números
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Guardamos el encoder para usarlo luego
joblib.dump(encoder, "label_encoder.pkl")

# 4. One-hot encoding
y_categorical = to_categorical(y_encoded)

# 5. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y_categorical, test_size=0.2, random_state=42
)

# 6. Crear modelo de red neuronal
model = Sequential([
    Dense(128, input_shape=(X.shape[1],), activation="relu"),
    Dropout(0.3),
    Dense(64, activation="relu"),
    Dropout(0.3),
    Dense(len(encoder.classes_), activation="softmax")
])

# 7. Compilar modelo
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# 8. Entrenar
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=30, batch_size=32)

# 9. Evaluar
loss, accuracy = model.evaluate(X_test, y_test)
print(f"✅ Precisión del modelo: {accuracy:.4f}")

# 10. Guardar modelo
model.save("hand_sign_model_keras.h5")
print("✅ Modelo guardado en hand_sign_model_keras.h5")