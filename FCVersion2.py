import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output


df = pd.read_excel('C:/Users/Chuck/Documents/Python Scripts/Python Project 1/May2020Transactions.xls')


app = dash.Dash()
features = df.columns



app.layout = html.Div([
            html.Div([
                dcc.Dropdown(id='xaxis',
                            options=[{'label':i,'value':i} for i in features],
                            value = ('Description'),
            ], style={'width':'48%','display':'inline-block'}),
            html.Div([
                dcc.Dropdown(id='yaxis',
                            options=[{'label':i,'value':i} for i in features],
                            value=('Amount')
            ],style={'width':'48%','display':'inline-block'}),
            dcc.Graph(id = 'May2020Transactions')


])

@app.callback(Output('May2020Transactions','figure'),
                [Input('xaxis','value'),
                Input('yaxis','value')])
def update_graph(xaxis_name,yaxis_name):
    return{'data':[go.Scatter(x=df[xaxis_name],
                              y=df[yaxis_name],
                              text=df['Description'],
                              mode='markers',
                              marker={'size':1000,
                              'opacity':0.5,
                              'line':{'width':0.5,'color':'white'}})
                              ]


    ,'layout':go.Layout(title='May2020Transactions',
                        xaxis={'title':xaxis_name},
                        yaxis={'title':yaxis_name})
                        }


if __name__ == '__main__':
    app.run_server()
