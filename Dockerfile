# Usamos Python 3.11 slim para mantener el contenedor ligero
FROM python:3.11-slim

# Instalar librerías del sistema necesarias para OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de la app dentro del contenedor
WORKDIR /app/Proyecto_TF/backend

# Copiar archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar tu app
CMD ["python", "app_server.py"]