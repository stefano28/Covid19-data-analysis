import dash_bootstrap_components as dbc
import dash_html_components as html

def card(title, value):
    card_content = [
        dbc.CardHeader(title),
        dbc.CardBody(
            [
                html.H5(value, className="card-title")
            ]
        ),
    ]
    return card_content

def progress_bar_ic(stats):
    pc = stats["last_ic"] * 100 / 6458
    progress = dbc.Progress(str(round(pc)) + "%", value=pc, striped=True, style={"height": "2rem"})
    return progress