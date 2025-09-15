# Usamos Python 3.11 slim
FROM python:3.11-slim

# Evitamos preguntas interactivas al instalar paquetes
ENV DEBIAN_FRONTEND=noninteractive

# Actualizamos e instalamos librerías necesarias para OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Creamos el directorio de la app
WORKDIR /app

# Copiamos todo el backend al contenedor
COPY . /app

# Instalamos dependencias de Python
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar tu app
CMD ["python", "app_server.py"]