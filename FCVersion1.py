import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash()


df = pd.read_excel('C:/Users/Chuck/Documents/Python Scripts/Python Project 1/May2020Transactions.xls')


app.layout = html.Div([dcc.Graph(id='May2020Transactions',figure={'data':[go.Scatter
                    (x=df['Description'],
                    y=df['Amount'],
                    mode='markers',
                    marker={
                    'size':3,
                    'color':'rgb(69,169,69)',
                    'symbol':'diamond','line':{'width':1}
                    })],
                    'layout':go.Layout(title = 'May2020Transactions'),
}),
            html.Hr(),
            html.Div([dcc.RadioItems(options=[
                    {'label':'Bank Account', 'value':'Bank'},
                    {'label':'Amount', 'value':'Amount'},
                    {'label':'Type', 'value':'Type'}],
                    value = 'Amount')])
], style={'fontFamily':'helvetica','fontSize':18})



if __name__ == '__main__':
    app.run_server()
