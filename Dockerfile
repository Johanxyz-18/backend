# Usamos Python 3.11 slim
FROM python:3.11-slim

# Instalar librerías del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de la app
WORKDIR /app

# Copiar archivos del proyecto
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar la app
CMD ["python", "app_server.py"]