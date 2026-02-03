"""
Fonctions de visualisation et génération de graphiques
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from utils.config import CLASS_COLORS, CLASSES

def create_probability_chart(probabilities):
    """
    Crée un graphique en barres des probabilités de prédiction
    
    Args:
        probabilities: dict {class_name: probability}
        
    Returns:
        Figure Plotly
    """
    classes = list(probabilities.keys())
    probs = list(probabilities.values())
    colors = [CLASS_COLORS.get(cls.upper(), "#69c8cf") for cls in classes]  


    
    fig = go.Figure(data=[
        go.Bar(
            x=classes,
            y=probs,
            marker_color=colors,
            text=[f'{p:.1%}' for p in probs],
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Probabilités de prédiction",
        xaxis_title="Classe",
        yaxis_title="Probabilité",
        yaxis=dict(range=[0, 1], tickformat='.0%'),
        height=400,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

def create_class_distribution_chart(class_counts):
    """
    Crée un graphique de distribution des classes
    
    Args:
        class_counts: dict {class_name: count}
        
    Returns:
        Figure Plotly
    """
    classes = list(class_counts.keys())
    counts = list(class_counts.values())
    colors = [CLASS_COLORS[cls.upper()] for cls in classes]
    
    fig = go.Figure(data=[
        go.Bar(
            x=classes,
            y=counts,
            marker_color=colors,
            text=counts,
            textposition='auto',
        )
    ])
    
    fig.update_layout(
        title="Distribution des images par classe",
        xaxis_title="Classe",
        yaxis_title="Nombre d'images",
        height=400,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

CLASSES = ["CRITICAL", "LOW", "NORMAL"]
CLASS_COUNTS  = {
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
CLASS_COLORS = {
    "NORMAL": "#2ecc71",
    "PNEUMONIA": "#e74c3c",
    "COVID": "#3498db"
}
def create_pie_chart(dataset_type="train"):
    """
    Crée un graphique circulaire de la distribution (valeurs en dur)
    """
    class_counts = CLASS_COUNTS[dataset_type]

    classes = list(class_counts.keys())
    counts = list(class_counts.values())
    colors = [CLASS_COLORS.get(cls, "#95a5a6") for cls in classes]

    fig = go.Figure(data=[go.Pie(
        labels=classes,
        values=counts,
        marker=dict(colors=colors),
        textinfo="label+percent+value",
        textfont_size=14,
        hole=0.3  # donut moderne (optionnel)
    )])

    fig.update_layout(
        title=f"Répartition des classes ({dataset_type})",
        height=400,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)"
    )

    return fig