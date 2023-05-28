# Previsao do Tempo em Python

O projeto consiste em desenvolver um aplicativo de linha de comando que obtém a previsão do tempo de uma determinada cidade ou do local atual com base no endereço IP. 

O aplicativo utiliza a API do OpenWeatherMap para obter os dados de previsão do tempo.

## Como Funciona

1) O usuário inicia o aplicativo.
2) O usuário fornece a chave de API do OpenWeatherMap e a cidade para a qual deseja obter a previsão do tempo ou deixa em branco para obter o tempo local.
3) O aplicativo utiliza a biblioteca geocoder para obter as coordenadas geográficas do local atual com base no endereço IP, caso a cidade não seja especificada.
4) Com base nas coordenadas geográficas ou na cidade fornecida, o aplicativo constrói a URL da API do OpenWeatherMap com a chave de API e faz uma solicitação GET para a API.
5) O aplicativo recebe a resposta da API em formato JSON e a analisa usando a biblioteca json.
6) Os dados relevantes da previsão do tempo, como temperatura e descrição, são extraídos da resposta JSON.
7) O aplicativo exibe os dados da previsão do tempo na saída, incluindo a cidade (se especificada) ou o local atual, temperatura e descrição.

## Rodando os testes

Para rodar os testes, rode o seguinte comando

1) Clone este repositório ou faça o download dos arquivos.
```bash
  git@github.com:Taunt-byte/Python-Previsao-do-Tempo.git
```

2) Execute esse comando.

```bash
  python main.py
```

## Licença

Este projeto está licenciado sob a MIT License.

[MIT](https://choosealicense.com/licenses/mit/)