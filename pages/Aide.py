"""
Page d'aide et documentation
"""

import streamlit as st
from utils.config import CUSTOM_CSS, CLASSES, CLASS_DESCRIPTIONS

st.set_page_config(page_title="Aide", page_icon="❓", layout="wide")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Titre
st.title("❓ Aide & Documentation")
st.markdown("Guide complet d'utilisation de l'application")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚀 Démarrage Rapide",
    "📖 Guide d'Utilisation",
    "🧠 À Propos du CNN",
    "❓ FAQ",
    "📞 Support"
])

# ==================== TAB 1: Démarrage Rapide ====================
with tab1:
    st.header("🚀 Démarrage Rapide")
    
    st.markdown("""
    ### Bienvenue dans l'application de classification des barrages! 👋
    
    Cette application utilise l'intelligence artificielle pour analyser les niveaux d'eau 
    des barrages de São Paulo à partir d'images satellite.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📋 Étapes pour Commencer
        
        1. **📊 Explorez les données**
           - Allez dans "Visualisation"
           - Découvrez les images du dataset
           - Filtrez par classe
        
        2. **🔮 Testez le modèle**
           - Allez dans "Prédiction"
           - Uploadez vos images
           - Obtenez des résultats instantanés
        
        3. **📈 Analysez les performances**
           - Consultez le "Dashboard"
           - Visualisez les métriques
           - Examinez les courbes
        
        4. **💾 Exportez vos résultats**
           - Téléchargez vos prédictions
           - Générez des rapports
           - Sauvegardez vos analyses
        """)
    
    with col2:
        st.markdown("""
        ### 🎯 Les 3 Classes
        """)
        
        for class_name in CLASSES:
            st.markdown(f"""
            **{class_name}**  
            {CLASS_DESCRIPTIONS[class_name.upper()]}
            """)
            st.markdown("")
        
        st.markdown("---")
        
        st.success("""
        **💡 Conseil** : Commencez par la page "Visualisation" 
        pour vous familiariser avec les images!
        """)
    
    st.markdown("---")
    
    # Video tutoriel (placeholder)
    st.subheader("🎥 Tutoriel Vidéo")
    
    st.info("📹 Une vidéo de démonstration sera bientôt disponible ici!")
    
    # Bouton d'action
    col1, col2= st.columns(2)
    
    with col1:
        if st.button("📊 Aller à Visualisation", use_container_width=True):
            st.switch_page("pages/Visualisation.py")
    
    with col2:
        if st.button("🔮 Aller à Prédiction", use_container_width=True):
            st.switch_page("pages/Prediction.py")
    

# ==================== TAB 2: Guide ====================
with tab2:
    st.header("📖 Guide d'Utilisation Complet")
    
    # Visualisation
    with st.expander("📊 Page Visualisation", expanded=True):
        st.markdown("""
        ### Objectif
        Explorer et visualiser les images du dataset d'entraînement et de test.
        
        ### Fonctionnalités
        - **Filtres** : Sélectionnez le type de dataset (train/test) et la classe
        - **Galerie** : Visualisez les images avec leurs étiquettes
        - **Statistiques** : Consultez la distribution des classes
        - **Graphiques** : Analysez la répartition des données
        
        ### Comment utiliser
        1. Sélectionnez le dataset (train ou test) dans la sidebar
        2. Choisissez une classe ou affichez toutes les classes
        3. Ajustez le nombre d'images à afficher
        4. Explorez la galerie d'images
        
        ### Astuces
        - Utilisez "Grande" taille pour voir plus de détails
        - Comparez les classes pour comprendre les différences
        - Notez les caractéristiques visuelles de chaque classe
        """)
    
    # Prédiction
    with st.expander("🔮 Page Prédiction"):
        st.markdown("""
        ### Objectif
        Faire des prédictions sur de nouvelles images de barrages.
        
        ### Fonctionnalités
        - **Upload multiple** : Analysez plusieurs images simultanément
        - **Prédiction en temps réel** : Résultats instantanés
        - **Scores de confiance** : Évaluez la fiabilité des prédictions
        - **Graphiques** : Visualisez les probabilités pour chaque classe
        
        ### Comment utiliser
        1. Cliquez sur "Browse files" pour uploader des images
        2. Sélectionnez une ou plusieurs images (.jpg, .png)
        3. Cliquez sur "Lancer la Prédiction"
        4. Consultez les résultats pour chaque image
        
        ### Astuces
        - Utilisez des images de qualité similaire au dataset
        - Vérifiez le score de confiance (> 60% recommandé)
        - Comparez les probabilités de toutes les classes
        - Uploadez plusieurs images pour gagner du temps
        """)
    
    # Dashboard
    with st.expander("📈 Page Dashboard"):
        st.markdown("""
        ### Objectif
        Analyser les performances et les métriques du modèle.
        
        ### Fonctionnalités
        - **Statistiques du dataset** : Nombre d'images, distribution
        - **Courbes d'entraînement** : Accuracy et loss par époque
        - **Matrice de confusion** : Erreurs de classification
        - **Métriques** : Precision, Recall, F1-Score
        
        ### Comment utiliser
        1. Consultez l'onglet "Dataset" pour les statistiques
        2. Analysez les courbes dans "Entraînement"
        3. Évaluez la performance dans "Performance"
        4. Exportez le rapport dans "Rapport"
        
        ### Astuces
        - Vérifiez l'équilibre des classes
        - Surveillez le surapprentissage (overfitting)
        - Comparez train vs validation accuracy
        - Identifiez les classes problématiques
        """)
    
    # Paramètres
    with st.expander("⚙️ Page Paramètres"):
        st.markdown("""
        ### Objectif
        Configurer le modèle et personnaliser l'application.
        
        ### Fonctionnalités
        - **Seuil de confiance** : Ajustez le niveau minimum
        - **Architecture** : Consultez la structure du CNN
        - **Gestion de fichiers** : Chargez de nouveaux modèles
        - **Cache** : Videz le cache si nécessaire
        
        ### Comment utiliser
        1. Ajustez le seuil de confiance selon vos besoins
        2. Consultez l'architecture dans l'onglet correspondant
        3. Uploadez un nouveau modèle si nécessaire
        4. Videz le cache en cas de problème
        
        ### Astuces
        - Seuil bas (40%) : Plus de prédictions, moins de fiabilité
        - Seuil haut (80%) : Moins de prédictions, plus de fiabilité
        - Consultez l'architecture pour comprendre le modèle
        - Sauvegardez l'ancien modèle avant d'en charger un nouveau
        """)
    
    # Téléchargement
    with st.expander("💾 Page Téléchargement"):
        st.markdown("""
        ### Objectif
        Exporter les résultats et générer des rapports.
        
        ### Fonctionnalités
        - **Export de prédictions** : CSV, JSON, Excel
        - **Rapports** : PDF, HTML
        - **Métadonnées** : Statistiques du dataset
        - **Archive complète** : Tous les fichiers
        
        ### Comment utiliser
        1. Faites d'abord des prédictions
        2. Allez dans "Téléchargement"
        3. Choisissez le format d'export
        4. Téléchargez les fichiers
        
        ### Astuces
        - CSV : Pour Excel et analyse de données
        - JSON : Pour intégration avec d'autres outils
        - PDF : Pour rapports professionnels
        - Exportez régulièrement pour garder un historique
        """)

# ==================== TAB 3: CNN ====================
with tab3:
    st.header("🧠 À Propos du Réseau de Neurones Convolutionnel")
    
    st.markdown("""
    ### 🎯 Qu'est-ce qu'un CNN?
    
    Un **CNN (Convolutional Neural Network)** est un type de réseau de neurones 
    particulièrement efficace pour l'analyse d'images. Il est conçu pour 
    détecter automatiquement des motifs visuels.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏗️ Architecture
        
        Notre CNN est composé de plusieurs types de couches :
        
        1. **Couches Convolutionnelles**
           - Détectent les caractéristiques (bords, textures)
           - Appliquent des filtres sur l'image
        
        2. **Couches de Pooling**
           - Réduisent la dimension des données
           - Conservent les informations importantes
        
        3. **Couches Fully Connected**
           - Combinent les caractéristiques
           - Produisent la classification finale
        
        4. **Couche de Sortie**
           - 3 neurones (1 par classe)
           - Activation Softmax pour les probabilités
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Fonctionnement
        
        **Étape 1 : Entrée**
        - Image 64×64×3 (RGB)
        - Pixels normalisés (0-1)
        
        **Étape 2 : Extraction de caractéristiques**
        - Filtres convolutionnels
        - Détection de motifs
        
        **Étape 3 : Réduction**
        - Pooling
        - Diminution de dimension
        
        **Étape 4 : Classification**
        - Couches denses
        - Probabilités par classe
        
        **Étape 5 : Prédiction**
        - Classe avec la probabilité max
        - Score de confiance
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🎓 Entraînement du Modèle
    
    Le modèle a été entraîné avec :
    - **4,581 images** d'entraînement (avec augmentation)
    - **100 images** de test
    - **Optimiseur** : Adam
    - **Fonction de perte** : Categorical Crossentropy
    - **Métriques** : Accuracy, Precision, Recall
    
    ### 🔬 Techniques Utilisées
    
    - **Data Augmentation** : Rotation, flip, transformations
    - **Normalisation** : Pixels entre 0 et 1
    - **Batch Normalization** : Stabilisation de l'entraînement
    - **Dropout** : Prévention du surapprentissage
    """)
    
    st.info("""
    💡 **Le saviez-vous?** Les CNNs ont révolutionné la vision par ordinateur
    et sont utilisés dans de nombreuses applications : reconnaissance faciale,
    voitures autonomes, diagnostic médical, et bien plus!
    """)

# ==================== TAB 4: FAQ ====================
with tab4:
    st.header("❓ Foire Aux Questions (FAQ)")
    
    # Questions générales
    st.subheader("🔷 Questions Générales")
    
    with st.expander("❓ Qu'est-ce que cette application?"):
        st.markdown("""
        C'est une application d'intelligence artificielle qui analyse automatiquement
        les images satellite des barrages de São Paulo pour déterminer leur niveau d'eau.
        Elle utilise un réseau de neurones convolutionnel (CNN) entraîné sur des données réelles.
        """)
    
    with st.expander("❓ Comment fonctionne la classification?"):
        st.markdown("""
        Le modèle analyse les caractéristiques visuelles de l'image (couleur, texture, forme)
        et compare avec ce qu'il a appris pendant l'entraînement pour déterminer si le niveau
        d'eau est Normal (>60%), Low (40-60%), ou Critical (<40%).
        """)
    
    with st.expander("❓ Quelle est la précision du modèle?"):
        st.markdown("""
        La précision dépend de plusieurs facteurs et peut être consultée dans le Dashboard.
        Le modèle a été entraîné sur 4,581 images et testé sur 100 images réelles.
        Consultez la page Dashboard pour les métriques détaillées.
        """)
    
    # Questions techniques
    st.subheader("🔷 Questions Techniques")
    
    with st.expander("❓ Quels formats d'images sont acceptés?"):
        st.markdown("""
        L'application accepte :
        - **JPG / JPEG**
        - **PNG**
        
        Résolution recommandée : 64×64 pixels, mais l'application peut redimensionner
        automatiquement les images.
        """)
    
    with st.expander("❓ Combien d'images puis-je uploader?"):
        st.markdown("""
        Vous pouvez uploader plusieurs images simultanément. Il n'y a pas de limite stricte,
        mais pour des performances optimales, nous recommandons de traiter par lots de 10-20 images.
        """)
    
    with st.expander("❓ Que signifie le score de confiance?"):
        st.markdown("""
        Le score de confiance représente la probabilité que la prédiction soit correcte :
        - **> 80%** : Très confiant, prédiction fiable
        - **60-80%** : Confiant, prédiction acceptable
        - **< 60%** : Peu confiant, vérification recommandée
        """)
    
    # Questions sur les données
    st.subheader("🔷 Questions sur les Données")
    
    with st.expander("❓ D'où viennent les données?"):
        st.markdown("""
        Les données proviennent d'images satellite des barrages de l'État de São Paulo, Brésil.
        Elles incluent 9 barrages des systèmes Cantareira, Guarapiranga, Alto Cotia, et autres.
        Les images sont composées de bandes NIR (Near Infrared), R (Red), et G (Green).
        """)
    
    with st.expander("❓ Qu'est-ce que l'augmentation des données?"):
        st.markdown("""
        L'augmentation des données est une technique qui crée de nouvelles images à partir
        des originales en appliquant des transformations (rotation, flip, etc.). Cela permet
        d'augmenter la taille du dataset et d'améliorer la robustesse du modèle.
        """)
    
    # Résolution de problèmes
    st.subheader("🔷 Résolution de Problèmes")
    
    with st.expander("❓ L'application est lente, que faire?"):
        st.markdown("""
        Quelques solutions :
        1. Réduisez le nombre d'images uploadées simultanément
        2. Utilisez des images de plus petite résolution
        3. Videz le cache dans Paramètres > Gestion de fichiers
        4. Rechargez l'application
        """)
    
    with st.expander("❓ Le modèle ne se charge pas"):
        st.markdown("""
        Vérifiez que :
        1. Le fichier `models/model.keras` existe
        2. Le fichier n'est pas corrompu
        3. Vous avez les bonnes versions de TensorFlow (2.15.0)
        4. Essayez de vider le cache et recharger
        """)
    
    with st.expander("❓ Les prédictions semblent incorrectes"):
        st.markdown("""
        Plusieurs raisons possibles :
        1. L'image est très différente du dataset d'entraînement
        2. Le score de confiance est faible (< 60%)
        3. L'image est de mauvaise qualité
        4. Le modèle n'a pas été entraîné sur ce type d'images
        
        Vérifiez toujours le score de confiance et les probabilités détaillées.
        """)

# ==================== TAB 5: Support ====================
with tab5:
    st.header("📞 Support & Contact")
    
    st.markdown("""
    ### 💬 Besoin d'aide?
    
    Si vous avez des questions, des problèmes ou des suggestions, voici comment nous contacter :
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📧 Contact
        
        - **Email** : kamnokamcher@gmail.com
        - **GitHub** : @RUTHKamno
        
        ### 🐛 Signaler un Bug
        
        Si vous rencontrez un problème :
        1. Notez les étapes pour reproduire le bug
        2. Prenez une capture d'écran si possible
        3. Envoyez-nous un email avec les détails
        
        ### 💡 Suggestions
        
        Vos idées sont les bienvenues!
        - Nouvelles fonctionnalités
        - Améliorations de l'interface
        - Optimisations du modèle
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Ressources
        
        - [Guide Complet (Dataset) ](https://www.kaggle.com/datasets/cerranet/volume-de-represas-de-so-paulo?resource=download-directory)
        
        ### 🔄 Mises à jour
        
        **Version actuelle** : 1.0.0
        
        **Prochainement** :
        - Export vers Google Sheets
        - API REST
        - Mode batch processing
        - Support multi-langues
        """)
    
    st.markdown("---")
    
    # Feedback
    st.subheader("💬 Feedback")
    
    st.markdown("Votre avis compte! Aidez-nous à améliorer l'application.")
    
    feedback_type = st.selectbox(
        "Type de feedback",
        ["Suggestion", "Bug", "Question", "Autre"]
    )
    
    feedback_text = st.text_area(
        "Votre message",
        placeholder="Partagez vos commentaires, suggestions ou problèmes...",
        height=150
    )
    
    if st.button("📤 Envoyer le Feedback", type="primary", width='stretch'):
        if feedback_text:
            st.success("✅ Merci pour votre feedback! Nous l'avons bien reçu.")
            st.balloons()
        else:
            st.warning("⚠️ Veuillez écrire un message avant d'envoyer.")


# Footer
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p><strong>🌊 Dam Classification Application</strong></p>
    <p>Version 1.0.0 | Développé avec ❤️ en utilisant Streamlit & TensorFlow</p>
    <p>© 2025 - Tous droits réservés</p>
</div>
""", unsafe_allow_html=True)

# Bouton de retour
if st.button("🏠 Retour à l'accueil", use_container_width=True):
    st.switch_page("app.py")