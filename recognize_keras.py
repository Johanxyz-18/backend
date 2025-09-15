import cv2
import mediapipe as mp
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Cargar modelo y encoder
model = load_model("hand_sign_model_keras.h5")
encoder = joblib.load("label_encoder.pkl")

# Configuración de MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Iniciar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar puntos
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extraer coordenadas normalizadas
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])

            # Convertir a numpy array
            X_input = np.array(landmarks).reshape(1, -1)

            # Predecir
            prediction = model.predict(X_input)
            class_id = np.argmax(prediction)
            letter = encoder.inverse_transform([class_id])[0]

            # Mostrar en pantalla
            cv2.putText(frame, f"Letra: {letter}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Reconocimiento de señas (Keras)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()