import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from googletrans import Translator

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Criação dos widgets da interface
        self.city_label = QLabel("Coloque o nome da cidade: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Previsão: ", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.translator = Translator()
        
        # Configura a interface do usuário
        self.initUI()

    def initUI(self):
        #  título 
        self.setWindowTitle("PREVISÃO")

        #layout vertical e adiciona os widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # alinhamento dos widgets
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # nomes dos objetos para a estilização
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # style dos widgets
        self.setStyleSheet(""" 
            QLabel, QPushButton{
                font-family: calibri;
            }         
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;      
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label{
                font-size: 75px;              
            }
            QLabel#emoji_label{
                font-size: 100px;
                font-family: Segoe UI emoji;      
            }
            QLabel#description_label{
               font-size: 20px; 
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        # Chave da API e URL para requisitar dados do clima no site OpenWeather
        api_key = "266e6e51d5a630e5d2e64b813eab6a77"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Verifica se a resposta foi bem-sucedida
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # Trata alguns erros HTTP específicos
            match response.status_code:
                case 400:
                    self.display_error("Não encontrado")
                case 401:
                    self.display_error("Acesso Negado:\n Chave Inválida")
                case 403:
                    self.display_error("Acesso Negado")
                case 404:
                    self.display_error("Cidade não encontrada")
                case 500:
                    self.display_error("Erro:\nTente novamente mais tarde")
                case 502:
                    self.display_error("Servidor sem resposta :(")
                case 503:
                    self.display_error("Serviço fora do ar")
                case 504:
                    self.display_error("Servidor lotado:\nSem resposta :(")
                case _:
                    self.display_error(f"Erro HTTP:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Erro de conexão\nVerifique se está conectado")
        except requests.exceptions.Timeout:
            self.display_error("Essa pesquisa demorou demais")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Muitas pesquisas\nRecarregue a página")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Erro de pesquisa:\n{req_error}")

    def display_error(self, message):
        # mensagens de erro
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_kel = data["main"]["temp"]
        temperature_cel = temperature_kel - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description_en = data["weather"][0]["description"]

        # Traduz a descrição do OpenWeather, que estão em inglês, para português
        weather_description_pt = self.translator.translate(weather_description_en, src='en', dest='pt').text

        self.temperature_label.setText(f"{temperature_cel:.0f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description_pt)
        self.description_label.setStyleSheet("font-size: 40px;")

    @staticmethod
    def get_weather_emoji(weather_id):
        # Retorna o emoji correspondente ao ID do clima
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 771: 
            return "🌬"
        elif weather_id == 781: 
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""

if __name__ == "__main__":
    # Cria a aplicação e a janela principal
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
