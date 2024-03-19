# Image de l'API basée sur une image python
FROM python:3.9-alpine

# Création et positionnement du répertoire par défaut dans le container
WORKDIR /app

# Copie du fichier requirements local (machine hôte) vers le container 
# (répertoire /app, car il s'agit du WORKDIR)
COPY requirements.txt requirements.txt

# Installation des dépendances dans le container
RUN pip install -r requirements.txt

# Copie de l'ensemble du code + dépendances
COPY . .

# Commande de démarrage du serveur gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--log-level", "info", "--error-logfile", "-", "--access-logfile", "-"]