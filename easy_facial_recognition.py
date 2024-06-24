import cv2

# Chargement du classificateur de visages pré-entrainé
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fonction pour détecter les visages dans une image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces

# Capture vidéo à partir de la webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture d'une frame
    ret, frame = cap.read()

    # Détection des visages dans la frame
    faces = detect_faces(frame)

    # Dessin des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Affichage de la frame
    cv2.imshow('Face Detection', frame)

    # Sortie de la boucle si la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libération des ressources
cap.release()
cv2.destroyAllWindows()
