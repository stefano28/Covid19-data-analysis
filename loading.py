import reading
import writing
import fitting
import datawrapper

def load():
    stats = reading.read_all()
    time_total = stats['time']
    intensive_care_total = stats['intensive_care']
    hospitalizations_total = stats['hospitalizations']
    time_last_month = []
    intensive_care_last_month = []
    hospitalizations_last_month = []
    time_last_month_back = []

    count = 0
    tme = 0
    m_ic = []
    q_ic = []
    m_h = []
    q_h = []

    inv = [0, 1, 2, 3, 4, 5, 6]

    for i in range(len(time_total) - 30, len(time_total)): 
        time_last_month.append(tme)
        intensive_care_last_month.append(intensive_care_total[i])
        hospitalizations_last_month.append(hospitalizations_total[i])
        count += 1
        tme += 1
        if(count > 6):
            time_last_month_back.append(time_total[i])
            m_ic.append(fitting.pol_just_slope(time_last_month, intensive_care_last_month))
            q_ic.append(fitting.pol_just_ins(inv, intensive_care_last_month))
            m_h.append(fitting.pol_just_slope(time_last_month, hospitalizations_last_month))
            q_h.append(fitting.pol_just_ins(inv, hospitalizations_last_month))
            time_last_month.pop(0)
            intensive_care_last_month.pop(0)
            hospitalizations_last_month.pop(0)
    
    writing.restore()

    for i in range(0, len(m_ic)):
        writing.update(time_last_month_back[i], m_ic[i], q_ic[i], m_h[i], q_h[i])


def load_saturation(stats):

    total_sat = []

    regions_ic = reading.read_regions_ic()

    count = 0

    for i in stats:
        region = {
            'id': "",
            'name': "",
            'saturation': "", 
        }
        region['id'] = i['codice_regione']
        region['name'] = regions_ic[count]['nome']
        region['saturation'] = round(i['terapia_intensiva']/regions_ic[count]['terapie_intensive'] *100, 2)
        total_sat.append(region)
        count +=  1

    writing.write_sat(total_sat)
    datawrapper.update()

    return total_sat