FROM python:3.11-slim

# Evitar preguntas interactivas y actualizar apt
ENV DEBIAN_FRONTEND=noninteractive

# Instalar librerías del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-utils \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de la app dentro del contenedor
WORKDIR /app

# Copiar archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar tu app
CMD ["python", "Proyecto_TF/backend/app_server.py"]