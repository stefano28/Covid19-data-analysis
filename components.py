import dash_bootstrap_components as dbc
import dash_html_components as html
import reading

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

def table():
    table_header = [
        html.Thead(html.Tr([html.Th("Giorno"), html.Th("Ricoveri"), html.Th("Terapie intensive")]))
    ]

    stats = reading.read_slope()

    n = len(stats['slope_ic']) - 1


    m_ic = stats['slope_ic'][n]
    q_ic = stats['ins_ic'][n]

    m_h = stats['slope_h'][n]
    q_h = stats['ins_h'][n]

    row1 = html.Tr([html.Td("Domani"), html.Td(m_h*7+q_h), html.Td(m_ic*7+q_ic)])
    row2 = html.Tr([html.Td("Dopo domani"), html.Td(m_h*8+q_h), html.Td(m_ic*8+q_ic)])
    row3 = html.Tr([html.Td("3 giorni"), html.Td(m_h*9+q_h), html.Td(m_ic*9+q_ic)])
    row4 = html.Tr([html.Td("4 giorni"), html.Td(m_h*10+q_h), html.Td(m_ic*10+q_ic)])

    table_body = [html.Tbody([row1, row2, row3, row4])]

    table = dbc.Table(table_header + table_body, bordered=True)
    return table