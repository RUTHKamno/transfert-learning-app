"""
Page de visualisation des images du dataset
"""

import streamlit as st
from utils.config import CUSTOM_CSS, CLASSES, CLASS_COLORS
from utils.data_utils import load_dataset_images, load_image_safe, get_dataset_statistics
from utils.visualization import create_class_distribution_chart, create_pie_chart
from types import SimpleNamespace

st.set_page_config(page_title="Visualisation", page_icon="📊", layout="wide")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Titre
st.title("📊 Visualisation des Images")
st.markdown("Explorez les images du dataset par classe et type")

st.markdown("---")

# Sidebar avec filtres
with st.sidebar:
    st.header("🔍 Filtres")
    
    # Type de dataset
    dataset_type = st.radio(
        "Type de dataset",
        ["train", "test"],
        format_func=lambda x: "🎓 Entraînement" if x == "train" else "🧪 Test"
    )
    
    # Filtre de classe
    class_filter = st.selectbox(
        "Classe",
        ["Toutes"] + CLASSES,
        help="Sélectionnez une classe spécifique ou toutes"
    )
    
    # Nombre d'images
    max_images = st.slider(
        "Images par classe",
        min_value=1,
        max_value=20,
        value=3,
        step=1,
        help="Nombre maximum d'images à afficher par classe"
    )
    
    # Taille d'affichage
    img_size = st.select_slider(
        "Taille des images",
        options=["Petite", "Moyenne", "Grande"],
        value="Moyenne"
    )

# Statistiques du dataset
st.subheader("📈 Statistiques du Dataset")

STATS = {
    "train": {
        "Normal": 2140,
        "Low": 1320,
        "Critical": 824
    },
    "test": {
        "Normal": 520,
        "Low": 410,
        "Critical": 194
    }
}

# stats = get_dataset_statistics(dataset_type)

stats = SimpleNamespace(
    train=SimpleNamespace(
        total_images=4284,
        Normal=SimpleNamespace(count=2140, total_images=4284),
        Low=SimpleNamespace(count=1320, total_images=4284),
        Critical=SimpleNamespace(count=824, total_images=4284),
    ),
    test=SimpleNamespace(
        total_images=1124,
        Normal=SimpleNamespace(count=520, total_images=1124),
        Low=SimpleNamespace(count=410, total_images=1124),
        Critical=SimpleNamespace(count=194, total_images=1124),
    )
)
current = getattr(stats, dataset_type)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total d'images", current.total_images)

with col2:
    st.metric("Classe Normal", current.Normal.count)

with col3:
    st.metric("Classe Low", current.Low.count)

with col4:
    st.metric("Classe Critical", current.Critical.count)

st.markdown("---")

# Galerie d'images
st.subheader("🖼️ Galerie d'Images")

# Déterminer le filtre de classe
selected_class = None if class_filter == "Toutes" else class_filter

# Charger les images
with st.spinner("Chargement des images..."):
    images = load_dataset_images(dataset_type, selected_class, max_images)
if not images:
    st.warning("⚠️ Aucune image trouvée. Vérifiez que le dossier data/ contient des images.")
else:
    st.success(f"✅ {len(images)} images chargées")
    
    # Déterminer le nombre de colonnes selon la taille
    cols_map = {"Petite": 6, "Moyenne": 4, "Grande": 3}
    num_cols = cols_map[img_size]
    
    # Afficher les images en grille
    cols = st.columns(num_cols)
    
    for idx, (img_path, class_name) in enumerate(images):
        col_idx = idx % num_cols
        
        with cols[col_idx]:
            img = load_image_safe(img_path)
            
            if img is not None:
                # Afficher l'image
                st.image(img, use_container_width=True)
                
                # Badge de classe coloré
                color = CLASS_COLORS[class_name.upper()]
                st.markdown(f"""
                <div style="
                    background-color: {color}22;
                    border-left: 4px solid {color};
                    padding: 8px;
                    border-radius: 5px;
                    margin-top: -10px;
                    text-align: center;
                ">
                    <strong style="color: {color};">{class_name}</strong>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("❌ Erreur de chargement")

st.markdown("---")

# Informations additionnelles
with st.expander("ℹ️ Informations sur les images"):
    st.markdown("""
    ### Composition des images
    - **Bandes spectrales** : NIR (Near Infrared), R (Red), G (Green)
    - **Résolution spatiale** : 2 mètres (après fusion panchromatique)
    - **Dimensions** : 224×224 pixels
    - **Format** : Images RGB composites
    
    ### Classes de classification
    - **Normal** : Volume du barrage > 60% de la capacité totale
    - **Low** : Volume entre 40% et 60% de la capacité
    - **Critical** : Volume < 40% de la capacité
    
    ### Augmentation des données
    Le dataset d'entraînement a été augmenté par :
    - Rotations
    - Retournements (flips)
    - Autres transformations géométriques
    """)

# Bouton de retour
if st.button("🏠 Retour à l'accueil", use_container_width=True):
    st.switch_page("app.py")