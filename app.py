import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import reading
import drawing
import components

stats = reading.read()

chart_1 = drawing.draw_chart_1(stats)
chart_2 = drawing.draw_chart_2(stats)
chart_3 = drawing.draw_chart_3(stats)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Covid19 data analysis' 
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
        dbc.Row(
            dbc.Col(
                dbc.Row(
                    [
                        dbc.Col(dbc.Card(components.card("Positivi su tamponi", str(stats["percetage_screening"]) + "%"), color="dark", inverse=True)),
                        dbc.Col(dbc.Card(components.card("Nuovi pazienti ricoverati", stats["last_h_var"]), color="dark", inverse=True)),
                        dbc.Col(dbc.Card(components.card("Nuovi pazienti in terapia intensiva", stats["last_ic_var"]), color="dark", inverse=True))

                    ],
                    className="mb-4",
                ),
            ),
            style = {
                'margin-top' : '5rem',
                'margin-left' : '10rem',
                'margin-right' : '10rem',
            }
        ),
        dbc.Row(
            dbc.Col(
                [
                html.H6(
                    children = "Terapie intensive occupate (solo pazienti Covid)",
                    style = {
                        'margin-top' : '3rem',
                        'margin-bottom' : '1.5rem'
                    }
                ),
                components.progress_bar_ic(stats)
                ]
            ),
            style = {
                'margin-left' : '10rem',
                'margin-right' : '10rem',
            }
        ),
        html.Div(
            children =  [
                dcc.Dropdown(
                    id= 'chart-dropdown',
                    options=[
                        {'label': 'Da inizio epidemia', 'value': 'GEN'},
                        {'label': 'Ultimo mese', 'value': 'LM'},
                        {'label': 'Ultima settimana', 'value': 'LW'},
                    ],
                    searchable=False,
                    value='GEN',
                    style = {
                        'width' : '20rem'
                    }
                ),
            ],
            style = {
                'padding-top' : '7rem',
                'padding-left' : '15rem',
            }
        ),
        html.Div(
            id = 'main-chart'
            )
        ]
    )

@app.callback(
    dash.dependencies.Output('main-chart', 'children'),
    [dash.dependencies.Input('chart-dropdown', 'value')])
def update_output(value):
    chart = chart_1
    if value == "LM":
        chart = chart_2
    elif value == "LW":
        chart = chart_3
    return dcc.Graph(
        figure=chart,
        style={
            'margin-left' : '10rem',
            'margin-right' : '10rem',
            'height' : '50rem'
        }
),

if __name__ == '__main__':
    app.run_server(debug=True)