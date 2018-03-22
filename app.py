from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def home():
    # return render_template('home.html')
    return render_template('map.html')
# the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

# """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True)
