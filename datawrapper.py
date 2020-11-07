import requests

def publish():
    url = "https://api.datawrapper.de/v3/charts/n02gP/publish"
    headers = {
        "Authorization": "Bearer aelzLABx3KGEcdGdhk1hBTrypJYTMAkje2xmexNLQm8e5GHAQsVQqneivIFURORK"
    }

    response = requests.request("POST", url, headers=headers)

def update():
    f = open("saturations.txt", "rt")
    url = "https://api.datawrapper.de/v3/charts/n02gP/data"


    headers = {
        "Authorization": "Bearer aelzLABx3KGEcdGdhk1hBTrypJYTMAkje2xmexNLQm8e5GHAQsVQqneivIFURORK",
        'content-type': "text/csv"
    }

    plaintext = f.read()

    response = requests.request("PUT", url, headers=headers, data=plaintext)

    publish()
