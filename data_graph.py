import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from dash import Dash, html, dcc

# Charger les données RATP
df = pd.read_csv('trafic-annuel-entrant-par-station-du-reseau-ferre-2021.csv', sep=';')
print(df.head())

# Top 10 des stations avec le plus grand trafic
top10 = df.groupby("Station").sum().sort_values("Trafic", ascending=False)[:10].reset_index()

# Trafic par ville (Top 5)
trafic_ville = df.groupby("Ville").sum().sort_values("Trafic", ascending=False)[:5].reset_index()

# Création de la figure pour le graphique à barres
fig_bar = go.Figure(data=[go.Bar(x=top10["Station"], y=top10["Trafic"], text=top10["Trafic"], textposition='auto')])
fig_bar.update_layout(title="TOP 10 stations with the biggest traffic")

# Création de la figure pour le graphique en camembert
fig_pie = px.pie(trafic_ville, values='Trafic', names='Ville', title='Pie chart trafic per cities')

# Création du layout de l'application
app = Dash(__name__)
app.layout = html.Div([
    html.H1("RATP data vizualisation"),
    html.Div([
        html.Div([
            dcc.Graph(id='graph_bar', figure=fig_bar,style={'background-color': 'green'})
        ], className="six columns"),
        html.Div([
            dcc.Graph(id='graph_pie', figure=fig_pie)
        ], className="six columns"),
    ], className="row")
])

# Lancement de l'application
if __name__ == '__main__':
    app.run_server(debug=True)
