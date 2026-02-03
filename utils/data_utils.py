"""
Utilitaires pour la gestion des données
"""

import os
import json
import pandas as pd
from PIL import Image
import streamlit as st
from utils.config import TRAIN_DATA_PATH, TEST_DATA_PATH, CLASSES

@st.cache_data
def load_dataset_images(dataset_type="train", class_filter=None, max_images=20):
    """
    Charge les images d'un dataset
    
    Args:
        dataset_type: "train" ou "test"
        class_filter: None (toutes) ou nom de classe spécifique
        max_images: Nombre maximum d'images par classe
        
    Returns:
        Liste de tuples (image_path, class_name)
    """
    base_path = TRAIN_DATA_PATH if dataset_type == "train" else TEST_DATA_PATH
    images = []
    
    # Déterminer quelles classes charger
    classes_to_load = [class_filter] if class_filter else CLASSES
    
    for class_name in classes_to_load:
        class_path = os.path.join(base_path, class_name)
        
        if not os.path.exists(class_path):
            continue
            
        # Lister tous les fichiers images
        image_files = [f for f in os.listdir(class_path) 
                      if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tif'))]
        
        # Limiter le nombre d'images
        image_files = image_files[:max_images]
        
        # Ajouter les chemins complets
        for img_file in image_files:
            images.append((os.path.join(class_path, img_file), class_name))
    
    return images

CLASSES = ["CRITICAL", "LOW", "NORMAL"]
HARDCODED_STATS = {
    "train": {
        "CRITICAL": 1369,
        "LOW": 1412,
        "NORMAL": 1503
    },
    "test": {
        "NORMAL": 343,
        "LOW": 354,
        "CRITICAL": 377
    }
}
def get_dataset_statistics(dataset_type="train"):
    """
    Calcule les statistiques du dataset (valeurs en dur)

    Returns:
        dict avec les statistiques
    """
    if dataset_type not in HARDCODED_STATS:
        raise ValueError("dataset_type doit être 'train' ou 'test'")

    class_counts = HARDCODED_STATS[dataset_type]

    stats = {
        "total_images": sum(class_counts.values()),
        "class_distribution": class_counts.copy()
    }

    return stats


def load_image_safe(image_path):
    """
    Charge une image de manière sécurisée
    
    Args:
        image_path: Chemin vers l'image
        
    Returns:
        PIL Image ou None en cas d'erreur
    """
    print( f"Chargement de l'image : {image_path}" )
    try:
        img = Image.open(image_path)
        return img.convert('RGB')
    except Exception as e:
        st.warning(f"Impossible de charger {image_path}: {str(e)}")
        return None