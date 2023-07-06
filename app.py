from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    month = datetime.now().month
    _, num_days = calendar.monthrange(year, month)
    days = list(range(1, num_days + 1))
    return render_template('home.html', days=days)

if __name__ == '__main__':
    app.run(debug=True)
