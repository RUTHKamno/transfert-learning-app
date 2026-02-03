"""
Page de prédiction sur nouvelles images
"""

import streamlit as st
from PIL import Image
import io
from utils.config import CUSTOM_CSS, CLASS_COLORS, CLASS_ICONS, CONFIDENCE_THRESHOLD
from utils.model_utils import load_model, predict_image
from utils.visualization import create_probability_chart

st.set_page_config(page_title="Prédiction", page_icon="🔮", layout="wide")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Titre
st.title("🔮 Prédiction sur Nouvelles Images")
st.markdown("Uploadez des images de barrages pour obtenir des prédictions")

st.markdown("---")

# Charger le modèle
model = load_model()

if model is None:
    st.error("❌ Le modèle n'est pas disponible. Veuillez vérifier le fichier model.keras dans le dossier models/")
    st.stop()

# Sidebar avec paramètres
with st.sidebar:
    st.header("⚙️ Paramètres")
    
    confidence_threshold = st.slider(
        "Seuil de confiance",
        min_value=0.0,
        max_value=1.0,
        value=CONFIDENCE_THRESHOLD,
        step=0.05,
        help="Niveau minimum de confiance pour considérer une prédiction comme fiable"
    )
    
    show_probabilities = st.checkbox(
        "Afficher toutes les probabilités",
        value=True,
        help="Affiche les probabilités pour toutes les classes"
    )
    
    st.markdown("---")
    st.info("""
    **💡 Conseils :**
    - Images au format JPG ou PNG
    - Résolution recommandée : 224×224
    - Images RGB ou niveaux de gris
    """)

# Upload d'images
st.subheader("📤 Upload d'Images")

uploaded_files = st.file_uploader(
    "Choisissez une ou plusieurs images",
    type=["jpg", "jpeg", "png",".tif"],
    accept_multiple_files=True,
    help="Vous pouvez uploader plusieurs images à la fois"
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} image(s) uploadée(s)")
    
    # Bouton de prédiction
    if st.button("🚀 Lancer la Prédiction", type="primary", use_container_width=True):
        
        st.markdown("---")
        st.subheader("📊 Résultats des Prédictions")
        
        # Barre de progression
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Traiter chaque image
        for idx, uploaded_file in enumerate(uploaded_files):
            # Mise à jour de la progression
            progress = (idx + 1) / len(uploaded_files)
            progress_bar.progress(progress)
            status_text.text(f"Analyse de l'image {idx + 1}/{len(uploaded_files)}...")
            
            # Charger l'image
            image = Image.open(uploaded_file)
            
            # Faire la prédiction
            result = predict_image(model, image)
            
            # Afficher les résultats
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.image(image, caption=uploaded_file.name, use_container_width=True)
            
            with col2:
                # Classe prédite
                predicted_class = result['class']
                confidence = result['confidence']
                color = CLASS_COLORS[predicted_class.upper()]
                icon = CLASS_ICONS[predicted_class.upper()]
                
                # Affichage avec badge coloré
                st.markdown(f"""
                <div style="
                    background: linear-gradient(135deg, {color}22 0%, {color}44 100%);
                    border-left: 5px solid {color};
                    padding: 20px;
                    border-radius: 10px;
                    margin-bottom: 20px;
                ">
                    <h2 style="color: {color}; margin: 0;">
                        {icon} Classe prédite : {predicted_class}
                    </h2>
                    <h3 style="color: #444; margin-top: 10px;">
                        Confiance : {confidence:.1%}
                    </h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Alerte si confiance faible
                if confidence < confidence_threshold:
                    st.warning(f"⚠️ Attention : La confiance ({confidence:.1%}) est inférieure au seuil ({confidence_threshold:.1%})")
                else:
                    st.success(f"✅ Prédiction fiable (confiance > {confidence_threshold:.1%})")
                
                # Graphique des probabilités
                if show_probabilities:
                    fig = create_probability_chart(result['probabilities'])
                    st.plotly_chart(fig, use_container_width=True)
                
                # Détails des probabilités
                with st.expander("📋 Détails des probabilités"):
                    for class_name, prob in result['probabilities'].items():
                        st.write(f"**{class_name}** : {prob:.2%}")
            
            st.markdown("---")
        
        # Fin du traitement
        progress_bar.empty()
        status_text.empty()
        st.balloons()
        st.success("🎉 Toutes les prédictions sont terminées !")

else:
    # Message d'instruction
    st.info("👆 Veuillez uploader une ou plusieurs images pour commencer")
    
    # Exemple visuel
    st.markdown("### 📸 Exemple d'images attendues")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **🟦 Normal**
        - Niveau d'eau élevé
        - Surface importante
        - Couleur claire
        """)
    
    with col2:
        st.markdown("""
        **🟨 Low**
        - Niveau intermédiaire
        - Surface réduite
        - Zones découvertes
        """)
    
    with col3:
        st.markdown("""
        **🟥 Critical**
        - Niveau très bas
        - Surface minimale
        - Zones sèches visibles
        """)

st.markdown("---")

# Informations supplémentaires
with st.expander("ℹ️ Comment fonctionne la prédiction ?"):
    st.markdown("""
    ### 🧠 Processus de prédiction
    
    1. **Prétraitement** : L'image est redimensionnée à 224×224 pixels et normalisée
    2. **Passage dans le CNN** : Le modèle analyse les caractéristiques de l'image
    3. **Classification** : Le modèle attribue des probabilités à chaque classe
    4. **Résultat** : La classe avec la probabilité la plus élevée est retournée
    
    ### 📊 Interprétation des résultats
    
    - **Confiance élevée (> 80%)** : Prédiction très fiable
    - **Confiance moyenne (60-80%)** : Prédiction acceptable
    - **Confiance faible (< 60%)** : Prédiction incertaine, vérification recommandée
    
    ### 🎯 Précision du modèle
    
    Le modèle a été entraîné sur 4,581 images et testé sur 100 images des barrages
    de São Paulo avec une augmentation des données pour améliorer la robustesse.
    """)

# Bouton de retour
if st.button("🏠 Retour à l'accueil", use_container_width=True):
    st.switch_page("app.py")