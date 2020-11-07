import urllib, json

def read_all():
    stats = {
        'time': [],
        'time_ita': [],
        'intensive_care': [], 
        'hospitalizations': [], 
        'last_total_screening': "", 
        'last_positive_cases': "", 
        'percetage_screening': "",
        'last_ic' : "",
        'last_ic_var': "",
        'last_h_var': ""
    }
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json") as url:
        response = url.read()
        data = json.loads(response.decode('utf-8'))
        i = 0
        for dic in data:
            time = dic['data'].split('T')
            stats['hospitalizations'].append(int(dic['ricoverati_con_sintomi']))
            stats['intensive_care'].append(int(dic['terapia_intensiva']))
            stats['time'].append(time[0])
            time_ita = str(time[0]).split('-')
            stats['time_ita'].append(time_ita[2] + '/' + time_ita[1] + '/' + time_ita[0])
            i = i + 1
        len_data = len(data) -1
        stats['last_ic_var'] = int(data[len_data]['terapia_intensiva']) - int(data[len_data - 1]['terapia_intensiva'])
        stats['last_h_var'] = int(data[len_data]['ricoverati_con_sintomi']) - int(data[len_data - 1]['ricoverati_con_sintomi'])
        stats['last_total_screening'] = int(data[len_data]['tamponi']) - int(data[len_data-1]['tamponi'])
        stats['last_ic'] = int(data[len_data]['terapia_intensiva'])
        stats['last_positive_cases'] = int(data[len_data]['nuovi_positivi'])
        stats['percetage_screening'] = round(int(data[len_data]['nuovi_positivi']) / stats['last_total_screening'] * 100, 2)
    return stats

def read_slope():
    stats = {
        'date': [], 
        'slope_ic': [],
        'ins_ic': [],
        'slope_h': [],
        'ins_h': []
    }
    with open('slope.json') as json_file: 
        data = json.load(json_file)
        for dic in data:
            stats['slope_h'].append(int(dic['slope_h']))
            stats['ins_h'].append(int(dic['ins_h']))
            stats['ins_ic'].append(int(dic['ins_ic']))
            stats['slope_ic'].append(int(dic['slope_ic']))
            stats['date'].append(dic['date'])
    return stats

def read_regions():
    with urllib.request.urlopen("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni-latest.json") as url:
        response = url.read()
        data = json.loads(response.decode('utf-8'))
        return data

def read_regions_ic():
    with open('intensive_care.json') as json_file: 
        data = json.load(json_file)
        return data