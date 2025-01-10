import socket
import time

# Configuration du serveur socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 9999))  # Hôte et port
server_socket.listen(1)  # Permettre une seule connexion client

print("Serveur socket en attente de connexion...")
conn, addr = server_socket.accept()  # Accepter la connexion

print(f"Connexion établie avec {addr}")

# Envoyer des données à intervalles réguliers
phrases = ['hello world', 'this is a test', 'spark streaming with socke', 'structured streaming example','La souris cherche la pomme', 'Le chien déteste le ballon', 'Le chien mange la maison', 'Le professeur construit le jardin', 'Le garçon voit le ballon', "L'éléphant aime le jardin", 'Le chien voit le travail', "L'éléphant mange le fromage", 'Le chien déteste le travail', 'La souris enseigne le fromage', "L'étudiant apprend la musique", "L'étudiant aime le livre", 'La fille mange le fromage', "La voiture apprend l'école", "L'éléphant aime la musique", "L'étudiant aime le livre", 'La voiture construit le livre', 'La voiture cherche le film', 'La souris aime le fromage', 'La souris détruit le jardin', "L'oiseau cherche le travail", 'Le professeur cherche le livre', "Le professeur mange l'école", "L'étudiant apprend le film", 'La fille voit la maison', 'Le professeur construit le ballon', "L'étudiant aime le ballon", "L'oiseau mange la maison", 'Le garçon cherche le film', "L'éléphant enseigne le film", 'La fille cherche le film', "L'éléphant détruit le fromage", 'Le garçon apprend la pomme', 'La voiture aime la musique', "L'éléphant détruit le ballon", 'Le chien mange le film', 'Le professeur déteste le film', 'Le chien déteste le travail', "L'étudiant détruit le ballon", "L'éléphant trouve la pomme", 'Le chat construit le livre', "L'oiseau apprend le jardin", 'La souris aime le jardin', 'Le professeur enseigne le film', 'Le professeur construit le jardin', 'Le chat voit la musique', "L'étudiant déteste le fromage", 'La voiture apprend la pomme', "L'étudiant construit la musique", 'Le garçon construit le livre', 'Le chat voit le ballon', 'Le chien construit le travail', "L'étudiant construit le livre", "L'éléphant enseigne le film", "L'étudiant apprend le film", 'Le chat mange la maison', 'La fille construit le fromage', "L'étudiant mange la maison", 'Le garçon enseigne le jardin', 'Le professeur apprend le fromage', "Le chien détruit l'école", "L'étudiant déteste la pomme", "L'éléphant trouve le travail", 'Le chat apprend le jardin', 'Le professeur mange le jardin', "L'éléphant déteste la musique", 'La voiture trouve la maison', 'Le professeur détruit la maison', 'Le chat mange la pomme', 'La voiture déteste la pomme', "L'étudiant enseigne le jardin", "L'étudiant détruit le film", 'Le chien voit le ballon', "L'oiseau trouve le film", "L'oiseau détruit la musique", "L'éléphant construit le jardin", "L'éléphant apprend la maison", 'La souris déteste le travail', 'La souris aime la musique', 'La voiture déteste le jardin', "Le garçon apprend l'école", "L'éléphant cherche le jardin", 'La souris apprend le travail', 'La fille mange la pomme', 'La souris déteste le fromage', 'La voiture apprend le ballon', "L'oiseau apprend l'école", "Le chien enseigne l'école", 'La voiture trouve la pomme', 'Le professeur cherche la musique', 'Le chat trouve la musique', 'La voiture détruit le fromage', "L'éléphant enseigne le jardin", "L'oiseau voit le jardin", "L'éléphant enseigne le livre", "L'étudiant enseigne le film", 'Le chat détruit le livre', 'Le chat aime le jardin', 'Le chat apprend le livre', "L'étudiant construit le livre"]
while True:
    for text in phrases:
        conn.send((text + "\n").encode())  # Envoyer un message avec un saut de ligne
        print(f"Envoyé : {text}")
        time.sleep(2)  # Pause de 2 secondes avant d'envoyer le prochain message

conn.close()
