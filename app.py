"""
Application Streamlit - Classification des Barrages de São Paulo
Page d'accueil principale
"""

import streamlit as st
from utils.config import CUSTOM_CSS, CLASSES, CLASS_ICONS, CLASS_DESCRIPTIONS, CLASS_COLORS
from utils.model_utils import load_model
from utils.data_utils import get_dataset_statistics

# Configuration de la page
st.set_page_config(
    page_title="Classification des Barrages - São Paulo",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Appliquer le CSS personnalisé
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Initialiser le modèle en cache
@st.cache_resource
def init_model():
    return load_model()

# Charger le modèle
model = init_model()

# === SIDEBAR ===
with st.sidebar:
    st.image("critical.tif", width='stretch')
    st.markdown("---")
    st.markdown("### 🧭 Navigation")
    st.markdown("""
    Utilisez les pages ci-dessous pour :
    - 📊 Visualiser les données
    - 🔮 Faire des prédictions
    - 📈 Voir les statistiques
    - ⚙️ Ajuster les paramètres
    - 💾 Télécharger les résultats
    - ❓ Obtenir de l'aide
    """)
    
    st.markdown("---")
    st.markdown("### ℹ️ À propos")
    st.info("""
    **Version:** 1.0.0  
    **Dataset:** Barrages de São Paulo  
    **Modèle:** CNN TensorFlow  
    **Images:** 64*64 pixels  
    """)

# === PAGE PRINCIPALE ===

# Titre principal
st.markdown('<h1 class="custom-title">🌊 Classification des Barrages de São Paulo</h1>', unsafe_allow_html=True)
st.markdown("### Application de deep learning pour la surveillance des niveaux d'eau")

st.markdown("---")

# Section de présentation
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## 🎯 Objectif du Projet")
    st.markdown("""
    Cette application utilise un **réseau de neurones convolutionnel (CNN)** pour classifier 
    automatiquement le niveau d'eau des barrages de l'État de São Paulo au Brésil à partir 
    d'images satellite.
    
    Les images sont composées de bandes spectrales **NIR** (Near Infrared), **R** (Red) et 
    **G** (Green) avec une résolution de **224×224 pixels**.
    
    ### 📍 Barrages analysés :
    - Système Cantareira : Atibainha, Jacareí, Jaguari
    - Système Guarapiranga : Billings
    - Système Alto Cotia : Pedro Beicht
    - Bassin de Sorocaba : Itupararanga, Barra Bonita
    - Bassin Ribeira de Iguape : Serraria
    """)

with col2:
    st.markdown("## 📊 Dataset")
    
    # Statistiques rapides
    train_stats = get_dataset_statistics("train")
    test_stats = get_dataset_statistics("test")
    
    st.metric("Images d'entraînement", train_stats['total_images'])
    st.metric("Images de test", test_stats['total_images'])
    st.metric("Nombre de classes", len(CLASSES))
    
    # Statut du modèle
    if model is not None:
        st.success("✅ Modèle chargé avec succès")
    else:
        st.error("❌ Modèle non disponible")

st.markdown("---")

# Section des classes
st.markdown("## 🏷️ Classes de Classification")

cols = st.columns(3)

for idx, class_name in enumerate(CLASSES):
    with cols[idx]:
        color = CLASS_COLORS[class_name.upper()]
        icon = CLASS_ICONS[class_name.upper()]
        desc = CLASS_DESCRIPTIONS[class_name.upper()]
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
            border-left: 5px solid {color};
            padding: 20px;
            border-radius: 10px;
            height: 100%;
        ">
            <h2 style="color: {color}; margin: 0;">{icon} {class_name}</h2>
            <p style="color: #444; margin-top: 10px; font-size: 0.9em;">{desc}</p>
            <p style="color: {color}; font-weight: bold; margin-top: 10px;">
                {train_stats['class_distribution'].get(class_name, 0)} images
            </p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Section des fonctionnalités
st.markdown("## 🚀 Fonctionnalités de l'Application")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 📊 Visualisation
    - Galerie d'images par classe
    - Filtres avancés
    - Aperçu du dataset
    """)
    
with col2:
    st.markdown("""
    ### 🔮 Prédiction
    - Upload d'images
    - Prédiction en temps réel
    - Scores de confiance
    """)
    
with col3:
    st.markdown("""
    ### 📈 Analyse
    - Métriques de performance
    - Courbes d'entraînement
    - Matrice de confusion
    """)

st.markdown("---")

# Call to action
st.markdown("## 🎬 Commencer")

col1, col2, col4 = st.columns(3)

with col1:
    if st.button("📊 Visualiser les données", use_container_width=True):
        st.switch_page("pages/Visualisation.py")

with col2:
    if st.button("🔮 Faire une prédiction", use_container_width=True):
        st.switch_page("pages/Prediction.py")

with col4:
    if st.button("❓ Aide", use_container_width=True):
        st.switch_page("pages/Aide.py")

st.markdown("---")

# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>Développé avec ❤️ en utilisant Streamlit & TensorFlow</p>
    <p>Dataset : Remote Sensing Image Patches - Barrages de São Paulo, Brésil</p>
</div>
""", unsafe_allow_html=True)