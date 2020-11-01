import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def draw_chart_1(stats):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=stats['time'],
        y=stats['intensive_care'],
        marker = dict(size=9),
        mode = 'markers',
        name = 'Terapie intensive'
        ))
    fig.add_trace(go.Scatter(
        x = stats['time'],
        y = stats['hospitalizations'],
        marker = dict(size=9),
        mode = 'markers',
        name = 'Ricoverati normali',
    ))
    fig.update_layout(
        title = 'Situazione ospedaliera Italiana',
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri'
    )
    return fig

def draw_chart_2(stats):
    fig = go.Figure()

    time_total = stats['time']
    intensive_care_total = stats['intensive_care']
    hospitalizations_total = stats['hospitalizations']
    time_last_month = []
    intensive_care_last_month = []
    hospitalizations_last_month = []

    for i in range(len(time_total) - 30, len(time_total)): 
        time_last_month.append(time_total[i])
        intensive_care_last_month.append(intensive_care_total[i])
        hospitalizations_last_month.append(hospitalizations_total[i])

    fig.add_trace(go.Scatter(
        x=time_last_month,
        y=intensive_care_last_month,
        marker = dict(size=9),
        mode = 'markers',
        name = 'Terapie intensive'
        ))
    fig.add_trace(go.Scatter(
        x = time_last_month,
        y = hospitalizations_last_month,
        marker = dict(size=9),
        mode = 'markers',
        name = 'Ricoverati normali',
    ))
    fig.update_layout(
        title = "Situazione ospedaliera nell'ultimo mese",
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri'
    )
    return fig