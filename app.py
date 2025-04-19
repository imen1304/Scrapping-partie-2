# app.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from data_loader import load_data

# Charger les données
df = load_data()

# Nettoyage / conversion
if "prix" in df.columns:
    df["prix"] = df["prix"].astype(str).str.replace(r"\D", "", regex=True)
    df["prix"] = pd.to_numeric(df["prix"], errors="coerce")

if "annee" in df.columns:
    df["annee"] = pd.to_numeric(df["annee"], errors="coerce")

if "kilometrage" in df.columns:
    df["kilometrage"] = df["kilometrage"].astype(str).str.replace(r"\D", "", regex=True)
    df["kilometrage"] = pd.to_numeric(df["kilometrage"], errors="coerce")

app = dash.Dash(__name__)

# Répartition par type de carburant
fig_carburant = px.pie(df, names="carburant", title="Répartition par type de carburant")

# Distribution des prix
fig_prix = px.histogram(df, x="prix", title="Distribution des prix", nbins=50)

# Répartition par boîte de vitesse
fig_boite = px.bar(df["boite"].value_counts().reset_index(), x="index", y="boite", title="Répartition des boîtes de vitesse")
fig_boite.update_layout(xaxis_title="Type de boîte", yaxis_title="Nombre d'annonces")

# Distribution des années
fig_annee = px.histogram(df, x="annee", title="Distribution des années", nbins=20)

app.layout = html.Div(children=[
    html.H1("Tableau de Bord des Annonces Automobiles", style={'textAlign': 'center'}),
    
    html.Div([
        dcc.Graph(figure=fig_carburant),
        dcc.Graph(figure=fig_prix)
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'flex-wrap': 'wrap'}),
    
    html.Div([
        dcc.Graph(figure=fig_boite),
        dcc.Graph(figure=fig_annee)
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'flex-wrap': 'wrap'})
])

if __name__ == '__main__':
    app.run(debug=True)
