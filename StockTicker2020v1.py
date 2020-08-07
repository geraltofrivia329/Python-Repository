import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div([
        html.H1("Stock Ticker Dashboard"),
        html.H3("Enter a Stock Symbol"),
        dcc.Input(id='my_stock_ticker',
                type="text",
                placeholder=""),
        dcc.Graph(id='my_graph',
                figure={
                'data':[
                {'x':[1,2,3], 'y':[4,5,6],'type':'line'}]
            }
        )


])

if __name__=='__main__':
    app.run_server()
