import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from datetime import datetime
from iexfinance.stocks import get_historical_data
import os


app = dash.Dash()

app.layout = html.Div([
        html.H1("Stock Ticker Dashboard"),
        dcc.Input(id='my_stock_ticker',
                value='TSLA'),
            dcc.Graph(id='my_graph',
            figure={'data':[
            {'x':[1,2,3], 'y':[4,5,6]}
            ], 'layout':{'title':'Default TItle'}}
            )
])

@app.callback(Output('my_graph','figure'),
            [Input('my_stock_ticker','value')])
def update_graph(StockData):
    start = datetime(2020,3,1)
    end = datetime(2020,6,24)
    os.environ["IEX_TOKEN"] = "pk_a3bffefd4f784874b9f9cff898578a74"
    df = get_historical_data(StockData,start=start,end=end,close_only=True, output_format='pandas')
    fig = {'data':[{'x':df.index,'y':df['close']}],
    'layout':{'title':StockData}
    }
    return fig


if __name__=='__main__':
    app.run_server()
