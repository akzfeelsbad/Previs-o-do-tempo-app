# Weather App

## Descrição

O **Weather App** é a minha primeira aplicação desenvolvida utilizando a linguagem Python. Basicamente ela permite ao usuário consultar a previsão do tempo para uma cidade específica. Utilizando a API OpenWeatherMap para obter os dados climáticos, a aplicação fornece informações sobre a temperatura e o clima atual.

## Funcionalidades

- **Entrada de Cidade**: Permite ao usuário inserir o nome de uma cidade que ele desejar.
- **Consulta de Clima**: Obtém a previsão do tempo da cidade inserida.
- **Exibição de Dados**: Mostra a temperatura atual e a descrição do tempo.
- **Tratamento de Erros**: Exibe mensagens de erro adequadas caso haja problemas com a consulta ou a conexão.

## Requisitos

Para executar este projeto, você precisará dos seguintes requisitos:

- Python 3.6 ou superior
- Bibliotecas Python:
  - `requests` para fazer as requisições HTTP
  - `PyQt5` para a interface gráfica
  - `googletrans` para tradução de textos (opcional)

## Instalação

- pip install requests PyQt5 googletrans==4.0.0-rc1

## Configuração
-Obtenha uma chave da API [OpenWeather](https://openweathermap.org):

  -Registre-se no OpenWeather e obtenha uma chave da API própia.
 
  -Substitua o valor da variável api_key no código Python pela sua chave da API.

-No arquivo weather_app.py, localize a linha e substitua pela sua chave:
    
    -api_key = "266e6e51d5a630e5d2e64b813eab6a77"


## Inspiração

 Esse projeto foi inspirado por este :) [Zerfallener-Succellus](https://github.com/Zerfallener-Succellus/GO-CLI-Weather-Forecast)

---


### Notas:
- **Chave da API**: Lembre-se de substituir `"266e6e51d5a630e5d2e64b813eab6a77"` pela sua própria chave da API OpenWeather antes de compartilhar o código.
- **Contato**: akyrisgermano@gmail.com



