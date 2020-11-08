import requests

def publish(id):
    url = "https://api.datawrapper.de/v3/charts/" + id + "/publish"
    headers = {
        "Authorization": "Bearer aelzLABx3KGEcdGdhk1hBTrypJYTMAkje2xmexNLQm8e5GHAQsVQqneivIFURORK"
    }

    response = requests.request("POST", url, headers=headers)

def update_sat():
    f = open("AppData/saturations.txt", "rt")
    url = "https://api.datawrapper.de/v3/charts/n02gP/data"


    headers = {
        "Authorization": "Bearer aelzLABx3KGEcdGdhk1hBTrypJYTMAkje2xmexNLQm8e5GHAQsVQqneivIFURORK",
        'content-type': "text/csv"
    }

    plaintext = f.read()
    plaintext.encode('utf-8')
    response = requests.request("PUT", url, headers=headers, data=plaintext)

    publish("n02gP")


def update_cap():
    f = open("AppData/capacities.txt", "rt")
    url = "https://api.datawrapper.de/v3/charts/2lDyq/data"


    headers = {
        "Authorization": "Bearer aelzLABx3KGEcdGdhk1hBTrypJYTMAkje2xmexNLQm8e5GHAQsVQqneivIFURORK",
        'content-type': "text/csv"
    }

    plaintext = f.read()
    plaintext.encode('utf-8')
    response = requests.request("PUT", url, headers=headers, data=plaintext)

    publish("2lDyq")