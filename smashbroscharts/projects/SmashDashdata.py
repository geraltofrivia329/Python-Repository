import dash
import dash_core_components as dcc
import dash_html_components as html
from django_plotly_dash import DjangoDash
import plotly.graph_objs as go
import pandas as pd

app = DjangoDash('SmashApp')

df = pd.read_excel('C:/Users/Chuck/Documents/Python Projects/SmashBros4.xlsx')

app.layout = html.Div([
            html.Div([dcc.Graph(id='smash-graph',
                                figure={'data': [go.Scatter(
                                x=df['Character'],
                                y=df['Score'],
                                mode = 'markers',
                                marker = {'size': 15,
                                        'opacity':0.5,})]}
                                )
        ])
])
