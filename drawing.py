import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import fitting

def draw_chart_1(stats):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=stats['time'],
        y=stats['intensive_care'],
        marker = dict(size=5),
        mode = 'markers',
        name = 'Terapie intensive'
        ))
    fig.add_trace(go.Scatter(
        x = stats['time'],
        y = stats['hospitalizations'],
        marker = dict(size=5),
        mode = 'markers',
        name = 'Ricoverati normali',
    ))
    fig.update_layout(
        title = 'Situazione ospedaliera Italiana da inizio epidemia',
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri',
        font=dict(
            size=15,
        )
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
        title = "Situazione ospedaliera Italiana nell'ultimo mese",
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri',
        font=dict(
            size=15,
        )
    )
    return fig

def draw_chart_3(stats):
    fig = go.Figure()

    time_total = stats['time']
    intensive_care_total = stats['intensive_care']
    hospitalizations_total = stats['hospitalizations']
    time_last_week = []
    intensive_care_last_week = []
    hospitalizations_last_week = []
    disc_time = []
    j = 0

    for i in range(len(time_total) - 7, len(time_total)):
        disc_time.append(j)
        j = j + 1
        time_last_week.append(time_total[i])
        intensive_care_last_week.append(intensive_care_total[i])
        hospitalizations_last_week.append(hospitalizations_total[i])

    f = fitting.pol(disc_time, hospitalizations_last_week)
    pol_x = f['x']
    pol_y = []
    for i in f['x']:
        pol_y.append(f['x'][i]*f['m'] + f['q'])

    fig.add_trace(go.Scatter(
        x=time_last_week,
        y=intensive_care_last_week,
        marker = dict(size=9),
        mode = 'markers',
        name = 'Terapie intensive'
        ))
    fig.add_trace(go.Scatter(
        x = time_last_week,
        y = hospitalizations_last_week,
        marker = dict(size=9),
        mode = 'markers',
        name = 'Ricoverati normali',
    ))
    fig.add_trace(go.Scatter(
        x= time_last_week,
        y = pol_y,
        mode='lines',
        name='Trendline ricoveri'
    ))
    fig.update_layout(
        title = "Situazione ospedaliera Italiana nell'ultimo mese",
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri',
        font=dict(
            size=15,
        )
    )
    return fig