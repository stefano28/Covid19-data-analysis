import plotly.graph_objects as go
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
        title = 'Situazione ospedaliera da inizio epidemia',
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
        title = "Situazione ospedaliera negli ultimi 30 giorni",
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

    f_h = fitting.pol(disc_time, hospitalizations_last_week)
    f_ic = fitting.pol(disc_time, intensive_care_last_week)
    result_h = []
    result_ic = []

    for i in f_h['x']:
        result_h.append(f_h['x'][i]*f_h['m'] + f_h['q'])

    for i in f_ic['x']:
        result_ic.append(f_ic['x'][i]*f_ic['m'] + f_ic['q'])

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
        y = result_h,
        mode='lines',
        name= 'y = ' + str(round(f_h['m'])) + 'x ' + '+ ' + str(round(f_h['q'])),
        line=dict(
                color='red', 
                width=4, 
                dash='dot'
            )
    ))
    fig.add_trace(go.Scatter(
        x= time_last_week,
        y = result_ic,
        mode='lines',
        name= 'y = ' + str(round(f_ic['m'])) + 'x ' + '+ ' + str(round(f_ic['q'])),
        line=dict(
                color='blue', 
                width=4, 
                dash='dot'
            )
    ))
    fig.update_layout(
        title = "Situazione ospedaliera Italiana negli ultimi 7 giorni",
        xaxis_title = 'Tempo',
        yaxis_title = 'Ricoveri',
        font=dict(
            size=15,
        )
    )
    return fig

def draw_chart_4(stats):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x= stats['date'],
        y = stats['slope_ic'],
        mode='lines+markers',
        name= 'Derivata terapie intensive',
    ))
    fig.add_trace(go.Scatter(
        x= stats['date'],
        y = stats['slope_h'],
        mode='lines+markers',
        name= 'Derivata ricoverati normali',
    ))
    fig.update_layout(
        title = "Andamento derivate negli ultimi 30 giorni",
        xaxis_title = 'Tempo',
        yaxis_title = 'Pendenza',
        font=dict(
            size=15,
        )
    )
    return fig