"""
Utilitaires pour le chargement et l'utilisation du modèle CNN
"""

import tensorflow as tf
import numpy as np
from PIL import Image
import streamlit as st
from utils.config import MODEL_PATH, IMG_SIZE, CLASSES

@st.cache_resource
def load_model():
    """
    Charge le modèle TensorFlow/Keras
    Utilise le cache de Streamlit pour éviter de recharger à chaque interaction
    """
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"❌ Erreur lors du chargement du modèle : {str(e)}")
        return None

def preprocess_image(image):
    """
    Prétraite une image pour la prédiction
    
    Args:
        image: PIL Image ou numpy array
        
    Returns:
        numpy array preprocessé de forme (1, 224, 224, 3)
    """
    # Convertir en PIL Image si nécessaire
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image.astype('uint8'))
    
    # Redimensionner à 224x224
    image = image.resize(IMG_SIZE)
    
    # Convertir en array numpy
    img_array = np.array(image)
    
    # S'assurer que l'image a 3 canaux
    if len(img_array.shape) == 2:  # Image en niveaux de gris
        img_array = np.stack([img_array] * 3, axis=-1)
    elif img_array.shape[2] == 4:  # Image RGBA
        img_array = img_array[:, :, :3]
    
    # Normaliser les valeurs de pixels (0-255 -> 0-1)
    img_array = img_array.astype('float32') / 255.0
    
    # Ajouter la dimension batch
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict_image(model, image):
    """
    Fait une prédiction sur une image
    
    Args:
        model: Modèle TensorFlow chargé
        image: PIL Image ou numpy array
        
    Returns:
        dict avec 'class', 'confidence' et 'probabilities'
    """
    # Prétraiter l'image
    processed_img = preprocess_image(image)
    
    # Faire la prédiction
    predictions = model.predict(processed_img, verbose=0)
    
    # Obtenir la classe prédite et sa confiance
    predicted_class_idx = np.argmax(predictions[0])
    confidence = predictions[0][predicted_class_idx]
    predicted_class = CLASSES[predicted_class_idx]
    
    # Créer un dictionnaire de probabilités par classe
    probabilities = {CLASSES[i]: float(predictions[0][i]) for i in range(len(CLASSES))}
    
    return {
        'class': predicted_class,
        'confidence': float(confidence),
        'probabilities': probabilities,
        'class_index': int(predicted_class_idx)
    }

def predict_batch(model, images):
    """
    Fait des prédictions sur un batch d'images
    
    Args:
        model: Modèle TensorFlow chargé
        images: Liste d'images PIL
        
    Returns:
        Liste de dictionnaires de prédictions
    """
    results = []
    for img in images:
        result = predict_image(model, img)
        results.append(result)
    return results

def get_model_summary():
    """
    Retourne un résumé du modèle sous forme de string
    """
    model = load_model()
    if model is None:
        return "Modèle non disponible"
    
    # Capturer le summary dans une string
    stringlist = []
    model.summary(print_fn=lambda x: stringlist.append(x))
    return "\n".join(stringlist)