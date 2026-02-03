"""
Configuration centrale de l'application
"""

# Chemins des fichiers
MODEL_PATH = "models/MobileNetV2 .h5"
TRAIN_DATA_PATH = "dataApp/train"
TEST_DATA_PATH = "dataApp/val"
# PREDICTIONS_PATH = "data/dataset/Teste/datasetTest_original"

# Paramètres du modèle
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
CONFIDENCE_THRESHOLD = 0.6

# Classes et leurs couleurs
CLASSES = ["Critical", "Low", "Normal"]
CLASS_COLORS = {
    "NORMAL": "#3B82F6",    # Bleu
    "LOW": "#FBBF24",       # Jaune
    "CRITICAL": "#EF4444"   # Rouge
}

CLASS_ICONS = {
    "NORMAL": "💧",
    "LOW": "⚠️",
    "CRITICAL": "🚨"
}

CLASS_DESCRIPTIONS = {
    "NORMAL": "Volume du barrage supérieur à 60% de la capacité totale",
    "LOW": "Volume du barrage entre 40% et 60% de la capacité totale",
    "CRITICAL": "Volume du barrage inférieur à 40% de la capacité totale"
}

# Style CSS personnalisé
CUSTOM_CSS = """
<style>
    /* Styles principaux */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Cartes */
    .metric-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
    }
    
    /* Badges de classe */
    .class-badge-normal {
        background-color: #DBEAFE;
        color: #1E40AF;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    .class-badge-low {
        background-color: #FEF3C7;
        color: #92400E;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    .class-badge-critical {
        background-color: #FEE2E2;
        color: #991B1B;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
    }
    
    /* Titre personnalisé */
    .custom-title {
        font-size: 3em;
        font-weight: bold;
        background: linear-gradient(90deg, #3B82F6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #1E3A8A 0%, #06B6D4 100%);
    }
    
    /* Boutons */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
</style>
"""