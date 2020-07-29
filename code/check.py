# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 10:19:19 2018

@author: swathisri.r
"""

import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'
    ),
    html.Div(id='output-container')
])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    if value=='NYC':
         return(html.A (href='http://localhost:9670'),)
    if value=='MTL':
         return(html.A(html.Button('click2',
                    id=1,style={'background':'#5F9EA0','font-weight':'bolder','color':'white','margin-top':'100px','border-radius': '50%','box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
    'margin-bottom': '100px',
    'margin-right': '100px',
    'margin-left': '200px','width':'200px','height':'200px'
    }),href='http://localhost:9670'),)
    if value=='MTL':
         return(html.A(html.Button('click3',
                    id=1,style={'background':'#5F9EA0','font-weight':'bolder','color':'white','margin-top':'100px','border-radius': '50%','box-shadow': '0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19)',
    'margin-bottom': '100px',
    'margin-right': '100px',
    'margin-left': '200px','width':'200px','height':'200px'
    }),href='http://localhost:9670'),)






if __name__ == '__main__':
    app.run_server(port=9221,debug=True)