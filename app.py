import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import reading
import drawing

stats = reading.read()

chart_1 = drawing.draw_chart_1(stats)
chart_2 = drawing.draw_chart_2(stats)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    children=[
        html.H1(
            children='Covid19 data analysis',
            style={
                'textAlign': 'center',
                'margin-top': '2rem'
            }
        ),
        html.H6(
            children='Stefano leggio',
            style={
                'textAlign': 'center',
            }
        ),
        dcc.Dropdown(
            id= 'chart-dropdown',
            options=[
                {'label': 'Situazione generale', 'value': 'GEN'},
                {'label': 'Ultimo mese', 'value': 'CU'},
            ],
            searchable=False,
            value='MTL'
        ),
        html.Div(
            id = 'main-chart',
            children = [
                    dcc.Graph(
                        figure=chart_1,
                        style={
                            'margin' : '10rem',
                            'height' : '70rem'
                        }
                    ),
                ]
            )
        ]
    )

@app.callback(
    dash.dependencies.Output('main-chart', 'children'),
    [dash.dependencies.Input('chart-dropdown', 'value')])
def update_output(value):
    chart = chart_1
    if value == "CU":
        chart = chart_2
    return dcc.Graph(
        figure=chart,
        style={
            'margin' : '10rem',
            'height' : '70rem'
        }
),

if __name__ == '__main__':
    app.run_server(debug=True)