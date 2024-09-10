# Utilisez l'image officielle de Python comme image de base
FROM python:3.12-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez le reste du code de l'application dans le conteneur
COPY . .

# Installez les dépendances
RUN pip install -r requirements.txt


# Exposez le port sur lequel l'application va tourner
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app",  "--port", "8000", "--host", "0.0.0.0" ]