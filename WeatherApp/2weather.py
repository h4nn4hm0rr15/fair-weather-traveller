from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/get_weather', methods=['POST'])
def weather():
    city_name = request.form['city_name']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=16a720ad9ccb6dc7f6c28e93aacc2962')
    json_object = r.json()
    weather = str(json_object['weather'][0]['main'])
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    temp_c = (temp_f - 32) * 5/9
    wind_speed = float(json_object['wind']['speed'])
    city = str(json_object['name'])
    return render_template('2temperature.html', main=weather, temp=temp_c, speed=wind_speed, city=city)


@app.route('/')
def index():
    return render_template('2index.html')

if __name__=='__main__':
    app.run(debug=True)
