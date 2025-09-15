# Instala flask, joblib y scikit-learn si no los tienes: pip install Flask joblib scikit-learn
import cv2
import numpy as np
import pickle
import tensorflow as tf
from flask import Flask, request, jsonify
from flask_cors import CORS 
import joblib 

app = Flask(__name__)
CORS(app) 

# Carga el modelo y el 'label encoder' una sola vez al iniciar el servidor
model = tf.keras.models.load_model('hand_sign_model_keras.h5')
with open('label_encoder.pkl', 'rb') as file:
    label_encoder = joblib.load(file)

@app.route('/reconocer', methods=['POST'])
def reconocer_senas():
    try:
        data = request.get_json()
        landmarks_data = data['landmarks']
        
        # El frontend envía una lista plana, la convertimos a un array de NumPy
        landmarks_np = np.array(landmarks_data)
        
        # La forma esperada del modelo es (1, 63)
        # Esto asegura que los datos tienen el formato correcto para tu modelo.
        landmarks_np = landmarks_np.reshape(1, 63)
        
        # Realiza la predicción con el modelo
        prediction = model.predict(landmarks_np)
        
        # Obtiene el índice de la predicción
        predicted_index = np.argmax(prediction)
        
        # Decodifica el índice para obtener la letra
        letra = label_encoder.inverse_transform([predicted_index])[0]
        
        print(f'Letra reconocida: {letra}')
        
        # Devuelve la letra como JSON
        return jsonify({'letra': str(letra)})
        
    except Exception as e:
        print(f'ocurrió un error: {e}')
        return jsonify({'error': 'Hubo un error en el servidor.'}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
