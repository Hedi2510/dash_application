# Image de base
FROM python:3.9-slim-buster

# Définit le répertoire de travail
WORKDIR /dash_application
#nom du fichier ou il ya tout les documents du projets réuni

# Copie le fichier requirements.txt dans l'image
COPY requirements.txt .

# Installe les dépendances
RUN pip install -r requirements.txt

# Copie tous les fichiers de l'application
COPY . .

# Expose le port 5000
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python3", "dash_application_final.py"]



#'docker build -t RATP_IDF_dash .' => pour créer l'image  dans docker

#'docker run -p 5000:5000 RATP_IDF_dash' => pour exécuter dans le conteneur dans docker

