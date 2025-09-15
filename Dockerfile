# Dockerfile para Render - Backend de lenguaje de señas
# Usamos Python 3.11 slim
FROM python:3.11-slim

# Evitamos que Python genere archivos pycache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos requirements.txt
COPY requirements.txt .

# Actualizamos pip e instalamos dependencias
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# Copiamos todo el código al contenedor
COPY . .

# Puerto en el que tu app Flask escuchará
EXPOSE 8000

# Comando para ejecutar tu app - reemplaza app.py si tu archivo principal tiene otro nombre
CMD ["python", "app.py"]