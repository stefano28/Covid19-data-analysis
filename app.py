import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import reading
import drawing
import components
import loading

stats = reading.read_all()
region_stats = reading.read_regions()
stats_slope = reading.read_slope()
loading.load()
chart_1 = drawing.draw_chart_1(stats)
chart_2 = drawing.draw_chart_2(stats)
chart_3 = drawing.draw_chart_3(stats)
chart_4 = drawing.draw_chart_4(stats_slope)

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
                [
                    html.H6(
                        children = "Dati del " + str(stats['time_ita'][len(stats['time_ita'])-1]),
                        style = {
                            'margin-top' : '3rem',
                            'margin-bottom' : '1.5rem'
                        }
                    ),
                    dbc.Row(
                        [
                            dbc.Col(dbc.Card(components.card("Positivi su tamponi", str(stats["percetage_screening"]) + "%"), color="dark", inverse=True)),
                            dbc.Col(dbc.Card(components.card("Nuovi positivi", stats["last_positive_cases"]), color="dark", inverse=True)),
                            dbc.Col(dbc.Card(components.card("Nuovi pazienti ricoverati", stats["last_h_var"]), color="dark", inverse=True)),
                            dbc.Col(dbc.Card(components.card("Nuovi pazienti in terapia intensiva", stats["last_ic_var"]), color="dark", inverse=True))

                        ],
                        className="mb-4",
                    ),
                ]
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
                        {'label': 'Ultimi 30 giorni', 'value': 'LM'},
                        {'label': 'Ultimi 7 giorni', 'value': 'LW'},
                        {'label': 'Andamento derivate', 'value': 'DD'},
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
        ),
        dbc.Row(
            dbc.Col(
                [
                    html.H6(
                        children = "Previsioni",
                        style = {
                            'margin-top' : '3rem',
                            'margin-bottom' : '1.5rem'
                        }
                    ),
                    components.table()
                ]
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
                    dcc.Dropdown(
                        id= 'datawrapper-dropdown',
                        options=[
                            {'label': 'Saturazione', 'value': 'STI'},
                            {'label': 'Capacità', 'value': 'CTI'},
                            {'label': 'Capacità su 100mila abitanti', 'value': 'GTI'},
                        ],
                        searchable=False,
                        value='STI',
                        style = {
                            'width' : '20rem',
                            'margin-bottom': '2rem'
                        }
                    ),
                    dbc.Button("Aggiorna", color="primary", id="update_dw", className="mr-1", style={"margin-bottom" : '2rem'}),
                    html.Div(
                        id = 'main-datawrapper'
                    ),
                    html.Div(
                        id = "output_btn"
                    )
                ]
            ),
            style = {
                    'margin-top' : '5rem',
                    'margin-left' : '10rem',
                    'margin-right' : '10rem',
            }
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
    elif value == "DD":
        chart = chart_4
    return dcc.Graph(
        figure=chart,
        style={
            'margin-left' : '10rem',
            'margin-right' : '10rem',
            'height' : '50rem'
        }
    ),

@app.callback(
    dash.dependencies.Output('main-datawrapper', 'children'),
    [dash.dependencies.Input('datawrapper-dropdown', 'value')])
def update_output(value):
    if value == "CTI":
        return html.Iframe(title="Capacità terapie intensive", style = {'height': '802px','min-width': '100%','border': 'none'}, src=f'https://datawrapper.dwcdn.net/2lDyq/')   
    if value == "STI":
        return html.Iframe(title="Saturazione terapie intensive", style = {'height': '802px','min-width': '100%','border': 'none'}, src=f'https://datawrapper.dwcdn.net/n02gP/')   
    if value == "GTI":
        return html.Iframe(title="Posti di terapia intensiva ogni 100mila abitanti", style = {'height': '802px','min-width': '100%','border': 'none'}, src=f'https://datawrapper.dwcdn.net/7qNQd/1/')   


@app.callback(
    dash.dependencies.Output("output_btn", "children"), 
    [dash.dependencies.Input("update_dw", 'n_clicks')]
)
def update_dw(n_clicks):
    loading.load_capacity()
    loading.load_saturation(region_stats)


if __name__ == '__main__':
    app.run_server(debug=True)