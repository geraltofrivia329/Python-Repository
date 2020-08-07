import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from datetime import datetime
from iexfinance.stocks import get_historical_data
import os


app = dash.Dash()

app.layout = html.Div([
        html.H1("Stock Ticker Dashboard"),
        html.Div([html.H3("Enter a stock symbol:",style={'paddingRight':'30px'}),
            dcc.Input(id='my_stock_ticker',
                value='TSLA',
                style={'fontSize':24,'width':75}
            )],style={'display':'inline-block','verticalAlign':'top'}),
        html.Button(id='submit-button',
                n_clicks=0,
                children='Submit Here',
                style={'fontSize':24}),

        html.Div([html.H3('Select a start and end date:'),
            dcc.DatePickerRange(
                id="my-date-picker-range",
                min_date_allowed=datetime(2020,3,1),
                max_date_allowed=datetime(2020,6,24),
                initial_visible_month=datetime(2020,3,1),
                start_date=datetime(2020,3,1),
                end_date=datetime(2020,6,24)
            ),
        ],style={'display':'inline-block'}),

            dcc.Graph(id='my_graph',
            figure={'data':[
            {'x':[1,2,3], 'y':[4,5,6]}
            ], 'layout':{'title':'Default TItle'}})


])

@app.callback(Output('my_graph','figure'),
            [Input('submit-button', 'n_clicks')],
                [State('my_stock_ticker','value'),
                State('my-date-picker-range','start_date'),
                State('my-date-picker-range','end_date')])
def update_graph(n_clicks,StockData,start_date,end_date):
    start = datetime.strptime(start_date[:10],'%Y-%m-%d')
    end = datetime.strptime(end_date[:10],'%Y-%m-%d')
    os.environ["IEX_TOKEN"] = "pk_a3bffefd4f784874b9f9cff898578a74"
    df = get_historical_data(StockData,start=start,end=end,close_only=True, output_format='pandas')
    fig = {'data':[{'x':df.index,'y':df['close']}],
    'layout':{'title':StockData}
    }
    return fig


if __name__=='__main__':
    app.run_server()
