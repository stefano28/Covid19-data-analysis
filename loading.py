import reading
import writing
import fitting

def load():
    stats = reading.read()
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

    h_slope = []
    ic_slope = []
    time = []
    j = 0


    for i in range(0, len(intensive_care_last_month)):
        ic_slope.append(intensive_care_last_month[i])
        time.append(i)
        #ic_slope.append(fitting.pol_just_slope(time, ic))
    ic_slope.append(fitting.pol_just_slope(time, ic))
    print(ic_slope)
"""
    j = 0

    for i in hospitalizations_last_month:
        h_slope.append(fitting.pol_just_slope(i, time_last_month[j]))
        j += 1
            j = 0

    while(j < 30):
        writing.write(time_last_month[j], ic_slope[j], h_slope[j])
        j += 1
"""

load()