# Usa una imagen oficial de Python como base.
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor.
WORKDIR /src

# Copia el archivo requirements.txt y lo instala.
COPY requirements.txt .

# Instala las dependencias del proyecto.
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación a /app.
COPY . .

# Expone el puerto 5000.
EXPOSE 5000

# Comando para ejecutar la aplicación.
CMD ["python", "app.py"]