from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather', methods=['POST'])
def weather():
    city_name = request.form['city_name']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=16a720ad9ccb6dc7f6c28e93aacc2962')
    json_object = r.json()
    weather = float(json_object['weather']['main'])
    return render_template('2temperature.html', main=weather)

@app.route('/temperature', methods=['POST'])
def temperature():
    city_name = request.form['city_name']
    print request.form
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=deb4c4aa994cc5ca9d606bd89e0c87d2')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('2temperature.html', temp=temp_f)

@app.route('/wind_speed', methods=['POST'])
def wind_speed():
    city_name = request.form['city_name']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=b8c9999ece863fc8ad2e5540425986cb')
    json_object = r.json()
    wind_speed = float(json_object['wind']['speed'])
    return render_template('2temperature.html', speed=wind_speed)


@app.route('/')
def index():
    return render_template('2index.html')

if __name__=='__main__':
    app.run(debug=True)
