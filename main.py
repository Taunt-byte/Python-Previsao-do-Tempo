import requests
import json
import geocoder

def obter_previsao_tempo_local(chave_api):
    g = geocoder.ip('me')
    if not g.ok:
        print("Não foi possível obter a localização.")
        return

    lat = g.latlng[0]
    lon = g.latlng[1]
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={chave_api}&units=metric"
    resposta = requests.get(url)
    dados = json.loads(resposta.text)

    if resposta.status_code == 200:
        cidade = dados['name']
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        print(f"Previsão do tempo em {cidade}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descrição: {descricao}")
    else:
        print("Não foi possível obter a previsão do tempo.")

chave_api = input("Digite sua chave de API: ")

obter_previsao_tempo_local(chave_api)
